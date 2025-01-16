import React, { useState } from 'react';
import { loginUser } from "../../service.ts/authservice"; // O serviço de login
import { z } from 'zod'; 

const LoginPage: React.FC = () => {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Validação com Zod
  const schema = z.object({
    email: z.string().email('Formato de email inválido'),
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
      setSuccess('Usuário logado com sucesso!');
      
    } catch (err: any) {
      // Lidar com erros de validação ou backend
      if (err instanceof z.ZodError) {
        setError(err.errors[0].message); // Exibe a primeira mensagem de erro
      } else {
        setError(err.message || 'Erro desconhecido');
      }
      setError(err || 'Erro ao fazer login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form className="w-full max-w-md bg-white p-8 shadow-lg rounded" onSubmit={handleSubmit}>
        <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>

        {error && <p className="text-red-500 text-center mb-4">{error}</p>}
        {success && <p className="text-green-500 text-center mb-4">{success}</p>}

        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2" htmlFor="email">
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="w-full border border-gray-300 rounded px-3 py-2"
            required
          />
        </div>

        <div className="mb-6">
          <label className="block text-gray-700 font-bold mb-2" htmlFor="password">
            Senha
          </label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className="w-full border border-gray-300 rounded px-3 py-2"
            required
          />
        </div>

        <button
          type="submit"
          className={`w-full bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 ${
            loading ? 'opacity-50 cursor-not-allowed' : ''
          }`}
          disabled={loading}
        >
          {loading ? 'Logando...' : 'Login'}
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
