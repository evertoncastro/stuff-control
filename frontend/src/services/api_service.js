import axios from 'axios';

const apiInstance = axios.create({
  baseURL: 'http://localhost:8000/api/',
  timeout: 10000,
});


apiInstance.interceptors.request.use(
  (config) => {
    const token = sessionStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default apiInstance