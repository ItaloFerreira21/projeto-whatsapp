import api from './api';

interface LoginData {
  email: string;
  password: string;
}

//função para registro de usuário
export const registerUser = async (userdata: { email: string; password: string; confirmPassword: string }) => {
  try {
    const response = await api.post('/auth/register', userdata);
    console.log("RESPOSTA DA API",response);
    return response.data;
  } catch (error: any) {
    console.log("ERRO DA API",error.response);
    return error.response ? error.response.data : { error: 'Erro desconhecido' };
  }
};

//outras funções de autenticação aqui 
//função para login de usuário
/* export const loginUser = async (userdata: { email: string; password: string }) => {
  try {
    const response = await api.post('/auth/login', userdata);
    console.log("RESPOSTA DA API",response);
    return response.data;
  } catch (error: any) {
    console.log("ERRO DA API",error.response);
    return error.response ? error.response.data : { error: 'Erro desconhecido' };
  }
}; */

//Implementação de Autenticação com JWT
export const loginUser = async (data: LoginData) => {
  try {
    const response = await api.post('/auth/login', data);
    const { token } = response.data.token;

    localStorage.setItem('auth.token', token);
    return response.data;

  } catch (error: any) {
    return error.response.data;
  }
}

