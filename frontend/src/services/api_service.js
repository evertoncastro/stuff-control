import axios from 'axios';

const apiInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
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