import axios from 'axios';

// Obter a URL base da API a partir da variável de ambiente
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

// Configuração da instância do axios
const api = axios.create({
  baseURL: apiBaseUrl, // Use a variável de ambiente para a URL base
  headers: {
    'Content-Type': 'application/json',
  },
});

// Função para registro de usuário
export const registerUser = async (userdata: { username: string; email: string; password: string; confirmPassword: string; cnpj: string; company_name?: string; phone_number?: string }) => {
  try {
    const response = await api.post('/auth/register', userdata);
    console.log("RESPOSTA DA API", response);
    return response.data;
  } catch (error: any) {
    console.log("ERRO DA API", error.response);
    return error.response ? error.response.data : { error: 'Erro desconhecido' };
  }
};

// Função para login de usuário
export const loginUser = async (userdata: { username: string; password: string }) => {
  try {
    const response = await api.post('/auth/login', userdata);
    const { token } = response.data;

    // Armazenar o token JWT no localStorage
    localStorage.setItem('auth.token', token);
    return response.data;
  } catch (error: any) {
    console.log("ERRO DA API", error.response);
    return error.response ? error.response.data : { error: 'Erro desconhecido' };
  }
};

// Função para obter o token JWT do localStorage
export const getToken = () => {
  return localStorage.getItem('auth.token');
};

// Configurar o axios para adicionar o token JWT ao cabeçalho de autorização
api.interceptors.request.use(
  (config) => {
    const token = getToken();
    console.log("Token usado na requisição:", token);

    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);