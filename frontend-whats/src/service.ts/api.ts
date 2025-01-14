import axios from 'axios';

// Obtenha a URL base do arquivo de ambiente
const baseURL = import.meta.env.VITE_API_BASE_URL;

// Configuração do Axios
const api = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
