import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import axios from 'axios';
import { toast } from 'react-toastify';

const loginSchema = yup.object().shape({
  email: yup.string().email('E-mail inválido').required('E-mail é obrigatório'),
  password: yup.string().min(6, 'A senha deve ter pelo menos 6 caracteres').required('Senha é obrigatória'),
});

const LoginPage = () => {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(loginSchema),
  });

  interface LoginFormInputs {
    email: string;
    password: string;
  }

  interface LoginResponse {
    data: {
      token: string;
      user: {
        id: string;
        email: string;
        name: string;
      };
    };
  }

  const onSubmit = async (data: LoginFormInputs) => {
    try {
      const response = await axios.post<LoginResponse>(`${import.meta.env.VITE_BACKEND_URL}/auth/login`, data);
      toast.success('Login realizado com sucesso!');
      console.log(response.data); // Aqui, você pode salvar o token no Context ou Zustand
    } catch (error) {
      toast.error('Erro ao fazer login. Verifique suas credenciais.');
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <form onSubmit={handleSubmit(onSubmit)} className="bg-white p-6 rounded shadow-md w-96">
        <h1 className="text-2xl font-bold mb-4">Login</h1>
        
        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">E-mail</label>
          <input
            {...register('email')}
            type="email"
            className="w-full p-2 border rounded focus:outline-none focus:ring"
          />
          {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>}
        </div>
        
        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">Senha</label>
          <input
            {...register('password')}
            type="password"
            className="w-full p-2 border rounded focus:outline-none focus:ring"
          />
          {errors.password && <p className="text-red-500 text-sm mt-1">{errors.password.message}</p>}
        </div>
        
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Entrar
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
