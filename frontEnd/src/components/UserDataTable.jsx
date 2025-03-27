import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";
import Swal from "sweetalert2";

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentUserEmail, setCurrentUserEmail] = useState(null);

  useEffect(() => {
    // Get current user email from JWT token
    const token = localStorage.getItem('accessToken');
    if (token) {
      const tokenData = JSON.parse(atob(token.split('.')[1]));
      setCurrentUserEmail(tokenData.email);
    }

    fetchUsers();
  }, []);

  const fetchUsers = () => {
    const token = localStorage.getItem('accessToken');
    axios
      .get("http://127.0.0.1:8000/users/api/", {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error cargando los datos:", error);
        setLoading(false);
      });
  };

  const handleDelete = async (id, email) => {
    // Prevent self-deletion
    if (email === currentUserEmail) {
      Swal.fire({
        icon: 'error',
        title: 'Operacoin Invalida',
        text: 'No puedes eliminar tu propia cuenta.'
      });
      return;
    }

    // Show confirmation dialog
    const result = await Swal.fire({
      title: 'Estas segura?',
      text: "Esta acion no se puede deshacer.",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Yes, eliminar...',
      cancelButtonText: 'Cancelar.'
    });

    if (result.isConfirmed) {
      try {
        const token = localStorage.getItem('accessToken');
        await axios.delete(`http://127.0.0.1:8000/users/api/${id}/`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        // Show success message
        await Swal.fire({
          icon: 'success',
          title: 'Eliminado!',
          text: 'El usuario ha sido eliminado con exito.'
        });

        // Refresh user list
        fetchUsers();
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Error al eliminar el usuario.'
        });
        console.error("Error al eliminar:", error);
      }
    }
  };

  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name,
      sortable: true,
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => alert(`Editando ${row.name}`)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row.id, row.email)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  return (
    <div>
      <h3>Tabla de usuarios</h3>
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