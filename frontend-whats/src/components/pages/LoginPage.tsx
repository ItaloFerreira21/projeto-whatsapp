import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from "../../service.ts/authservice"; // O serviço de login
import { z } from 'zod'; 

const LoginPage: React.FC = () => {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  // Validação com Zod
  const schema = z.object({
    username: z.string().min(1, 'Username é obrigatório'),
    password: z.string().min(8, 'Senha deve ter no mínimo 8 caracteres'),
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');

    try {
      // Validação com Zod
      schema.parse(formData);

      const result = await loginUser(formData); 
      console.log('Resultado:', result); // Apenas para debug
      if (result.error) {
        setError(result.error);
      } else {
        setSuccess('Usuário logado com sucesso!');
        navigate('/dashboard');  // Redirecionar para o DashboardPage
      }
      
    } catch (err: any) {
      // Lidar com erros de validação ou backend
      if (err instanceof z.ZodError) {
        setError(err.errors[0].message);
      } else {
        setError('Erro desconhecido');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 space-y-6 bg-white rounded shadow-md">
        <h2 className="text-2xl font-bold text-center">Login</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Username:</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 mt-1 border rounded-md shadow-sm focus:outline-none focus:ring focus:ring-indigo-200"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Password:</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 mt-1 border rounded-md shadow-sm focus:outline-none focus:ring focus:ring-indigo-200"
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full px-4 py-2 font-bold text-white bg-indigo-600 rounded hover:bg-indigo-700 focus:outline-none focus:ring focus:ring-indigo-200"
          >
            {loading ? 'Carregando...' : 'Login'}
          </button>
        </form>
        {error && <p className="mt-4 text-sm text-red-600">{error}</p>}
        {success && <p className="mt-4 text-sm text-green-600">{success}</p>}
      </div>
    </div>
  );
};

export default LoginPage;