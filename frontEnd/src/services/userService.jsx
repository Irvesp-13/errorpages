import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/users/api/";

// Helper function to get new access token using refresh token
const refreshAccessToken = async () => {
    try {
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post('http://127.0.0.1:8000/users/token/refresh/', {
            refresh: refreshToken
        });
        localStorage.setItem('accessToken', response.data.access);
        return response.data.access;
    } catch (error) {
        // If refresh fails, logout user
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        window.location.href = '/login';
        throw error;
    }
};

// Axios interceptor to handle token refresh
axios.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const newToken = await refreshAccessToken();
            originalRequest.headers['Authorization'] = `Bearer ${newToken}`;
            return axios(originalRequest);
        }
        return Promise.reject(error);
    }
);

export const deleteUser = async (userId, currentUserId) => {
    if (userId === currentUserId) {
        throw new Error("You cannot delete your own account!");
    }
    
    const token = localStorage.getItem('accessToken');
    return axios.delete(`${API_URL}${userId}/`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
};

export const updateUser = async (userId, userData) => {
    const token = localStorage.getItem('accessToken');
    return axios.put(`${API_URL}${userId}/`, userData, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
};

export const getCurrentUser = async () => {
    const token = localStorage.getItem('accessToken');
    return axios.get(`${API_URL}me/`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
};