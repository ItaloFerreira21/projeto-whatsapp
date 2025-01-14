import React, { useState } from 'react';
import { registerUser } from "../../service.ts/authservice";
const RegisterPage: React.FC = () => {
  const [formData, setFormData] = useState({ email: '', password: '', conformPassword: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');

    if (formData.password !== formData.conformPassword) {
      setError('Senhas não conferem');
      setLoading(false);
      return;
    }

    try {
      const result = await registerUser(formData);
      setSuccess('Usuário registrado com sucesso!');
      console.log('Resultado:', result); // Apenas para debug
    } catch (err: any) {
      setError(err || 'Erro desconhecido');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form className="w-full max-w-md bg-white p-8 shadow-lg rounded" onSubmit={handleSubmit}>
        <h2 className="text-2xl font-bold mb-6 text-center">Registrar</h2>

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

        <div className="mb-4">
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

        <div className='mb-4'>
          <label className="block text-gray-700 font-bold mb-2" htmlFor="conformPassword">
            Confirmar Senha
          </label>
          <input
            type="password"
            id="conformPassword"
            name="conformPassword"
            value={formData.conformPassword}
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
          {loading ? 'Registrando...' : 'Registrar'}
        </button>
      </form>
    </div>
  );
};

export default RegisterPage;
