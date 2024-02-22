import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:5555/api';

const api = axios.create({
  baseURL: BASE_URL,
});

export const fetchUsers = () => api.get('/users');
export const fetchUser = (userId) => api.get(`/user/${userId}`);

export const fetchEvents = () => api.get('/events');
export const fetchEvent = (eventId) => api.get(`/event/${eventId}`);

export const fetchAuthorizations = () => api.get('/authorizations');

export const registerUser = async (userData) => {
  try {
    const response = await api.post('/register', userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const getAllUsers = async () => {
  try {
    const response = await api.get('/users');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
export const getAllEvents = async () => {
    try {
      const response = await api.get('/events');
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  };
export default api;