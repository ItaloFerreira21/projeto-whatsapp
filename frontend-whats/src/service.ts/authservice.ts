import api from './api';

//função para registro de usuário
export const registerUser = async (userdata: { email: string; password: string }) => {
  try {
    const response = await api.post('/auth/register', userdata);
    return response.data;
  } catch (error: any) {
    return error.response.data;
  }
};

//outras funções de autenticação aqui 
//função para login de usuário
export const loginUser = async (userdata: { email: string; password: string }) => {
  try {
    const response = await api.post('/auth/login', userdata);
    return response.data;
  } catch (error: any) {
    return error.response.data;
  }
};