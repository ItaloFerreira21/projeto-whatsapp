import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { getToken } from '../../service.ts/authservice'; // Certifique-se de que o caminho está correto

// Definir os tipos para o Freelancer e a resposta da API
interface Freelancer {
  id: number;
  nome_completo: string;
  celular: string;
  sexo: string;
  email: string;
  rg: string;
  chave_pix: string | null;
}

interface NewFreelancer {
  nome_completo: string;
  celular: string;
  sexo: string;
  email: string;
  rg: string;
  chave_pix: string;
}

const DashboardPage: React.FC = () => {
  const [freelancers, setFreelancers] = useState<Freelancer[]>([]);
  const [newFreelancer, setNewFreelancer] = useState<NewFreelancer>({
    nome_completo: '',
    celular: '',
    sexo: '',
    email: '',
    rg: '',
    chave_pix: ''
  });

  useEffect(() => {
    const token = getToken();
    console.log('Token enviado:', token); // Verifique se o token é válido
    axios.get('http://localhost:5000/api/freelancers', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then((response: AxiosResponse<Freelancer[]>) => {
      console.log('Resposta da API:', response.data);  // Confirme se a resposta é correta
      setFreelancers(response.data);
    })
    .catch(error => {
      console.error('Erro ao buscar freelancers:', error);
    });
  }, []);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setNewFreelancer(prevState => ({
      ...prevState,
      [name]: value || ''
    }));
  };

  const handleAddFreelancer = () => {
    const token = getToken();
    console.log('Token usado na requisição:', token);
    
    axios.post<Freelancer>('http://localhost:5000/api/freelancers', newFreelancer, {
      headers: { Authorization: `Bearer ${token}` },
      withCredentials: true
    })
    .then((response: AxiosResponse<Freelancer>) => {
      console.log('Freelancer adicionado:', response.data);
      setFreelancers(prevState => [...prevState, response.data]);
      setNewFreelancer({
        nome_completo: '',
        celular: '',
        sexo: '',
        email: '',
        rg: '',
        chave_pix: ''
      });
    })
    .catch(error => {
      console.error('Erro ao adicionar freelancer:', error);
    });
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard do Contratante</h1>
      <div className="mb-4">
        <input
          type="text"
          name="nome_completo"
          value={newFreelancer.nome_completo}
          onChange={handleInputChange}
          placeholder="Nome Completo"
          className="border p-2 rounded mb-2"
        />
        <input
          type="text"
          name="celular"
          value={newFreelancer.celular}
          onChange={handleInputChange}
          placeholder="Celular"
          className="border p-2 rounded mb-2"
        />
        <input
          type="text"
          name="sexo"
          value={newFreelancer.sexo}
          onChange={handleInputChange}
          placeholder="Sexo"
          className="border p-2 rounded mb-2"
        />
        <input
          type="email"
          name="email"
          value={newFreelancer.email}
          onChange={handleInputChange}
          placeholder="Email"
          className="border p-2 rounded mb-2"
        />
        <input
          type="text"
          name="rg"
          value={newFreelancer.rg}
          onChange={handleInputChange}
          placeholder="RG"
          className="border p-2 rounded mb-2"
        />
        <input
          type="text"
          name="chave_pix"
          value={newFreelancer.chave_pix}
          onChange={handleInputChange}
          placeholder="Chave PIX"
          className="border p-2 rounded mb-2"
        />
        <button
          onClick={handleAddFreelancer}
          className="bg-blue-500 text-white p-2 rounded"
        >
          Adicionar Freelancer
        </button>
      </div>
      <div className="space-y-4">
        {Array.isArray(freelancers) && freelancers.map(freelancer => (
          <div key={freelancer.id} className="border p-4 rounded">
            <p><strong>Nome:</strong> {freelancer.nome_completo}</p>
            <p><strong>Celular:</strong> {freelancer.celular}</p>
            <p><strong>Email:</strong> {freelancer.email}</p>
            <p><strong>RG:</strong> {freelancer.rg}</p>
            <p><strong>Chave PIX:</strong> {freelancer.chave_pix || 'Não informada'}</p>
            {/* Adicione botões para editar ou excluir */}
          </div>
        ))}
      </div>
    </div>
  );
};

export default DashboardPage;