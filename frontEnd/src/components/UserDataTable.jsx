import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";
import Swal from "sweetalert2";

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentUserEmail, setCurrentUserEmail] = useState(null);
  const [editingUser, setEditingUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      const tokenData = JSON.parse(atob(token.split('.')[1]));
      setCurrentUserEmail(tokenData.email);
    }
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await axios.get("http://127.0.0.1:8000/users/api/", {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      setData(response.data);
      setLoading(false);
    } catch (error) {
      if (error.response?.status === 401) {
        await refreshToken();
        fetchUsers();
      } else {
        console.error("Error cargando usuaruis:", error);
        setLoading(false);
      }
    }
  };

  const refreshToken = async () => {
    try {
      const refreshToken = localStorage.getItem('refreshToken');
      const response = await axios.post('http://127.0.0.1:8000/users/token/refresh/', {
        refresh: refreshToken
      });
      localStorage.setItem('accessToken', response.data.access);
      return response.data.access;
    } catch (error) {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      window.location.href = '/login';
    }
  };

  const handleDelete = async (id, email) => {
    if (email === currentUserEmail) {
      Swal.fire({
        icon: 'error',
        title: 'Operacion no permitida',
        text: 'No puedes borrar tu propia cuenta!'
      });
      return;
    }

    const result = await Swal.fire({
      title: 'Estas seguro?',
      text: "No puedes revertir esta accion!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Borrar!',
      cancelButtonText: 'Cancelar'
    });

    if (result.isConfirmed) {
      try {
        const token = localStorage.getItem('accessToken');
        await axios.delete(`http://127.0.0.1:8000/users/api/${id}/`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        await Swal.fire({
          icon: 'success',
          title: 'Borrado!',
          text: 'El usuario se borro de forma exitosa.'
        });

        fetchUsers();
      } catch (error) {
        if (error.response?.status === 401) {
          await refreshToken();
          handleDelete(id, email);
        } else {
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'El usuario no pudo ser borrado.'
          });
        }
      }
    }
  };

  const handleEdit = async (user) => {
    const { value: formValues } = await Swal.fire({
      title: 'Edit User',
      html:
        `<input id="name" class="swal2-input" placeholder="Name" value="${user.name || ''}" >` +
        `<input id="email" class="swal2-input" placeholder="Email" value="${user.email || ''}" >` +
        `<input id="tel" class="swal2-input" placeholder="Telefono" value="${user.tel || ''}" >` +
        `<input id="age" class="swal2-input" type="number" placeholder="Edad" value="${user.age || ''}" >`,
      focusConfirm: false,
      showCancelButton: true,
      confirmButtonText: 'Actualizar',
      preConfirm: () => {
        return {
          name: document.getElementById('name').value,
          email: document.getElementById('email').value,
          tel: document.getElementById('tel').value,
          age: document.getElementById('age').value
        }
      }
    });

    if (formValues) {
      const confirmResult = await Swal.fire({
        title: 'Estas seguro?',
        text: "Quieres actualizar este usuario?",
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Actualizar'
      });

      if (confirmResult.isConfirmed) {
        try {
          const token = localStorage.getItem('accessToken');
          await axios.put(`http://127.0.0.1:8000/users/api/${user.id}/`, formValues, {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });

          await Swal.fire({
            icon: 'success',
            title: 'Actualizado!',
            text: 'El usuario ha sido actualizado correctamente.'
          });

          fetchUsers();
        } catch (error) {
          if (error.response?.status === 401) {
            await refreshToken();
            handleEdit(user);
          } else {
            Swal.fire({
              icon: 'error',
              title: 'Error',
              text: 'Error al actualizar el usuario.'
            });
          }
        }
      }
    }
  };

  const columns = [
    {
      name: "Name",
      selector: (row) => row.name,
      sortable: true,
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Phone",
      selector: (row) => row.tel,
    },
    {
      name: "Age",
      selector: (row) => row.age,
    },
    {
      name: "Actions",
      cell: (row) => (
        <div className="btn-group">
          <button
            className="btn btn-warning btn-sm"
            onClick={() => handleEdit(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger btn-sm ms-2"
            onClick={() => handleDelete(row.id, row.email)}
            disabled={row.email === currentUserEmail}
          >
            <i className="bi bi-trash"></i>
          </button>
        </div>
      ),
    },
  ];

  return (
    <div className="container mt-4">
      <h3>User Management</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
    </div>
  );
};

export default UserDataTable;