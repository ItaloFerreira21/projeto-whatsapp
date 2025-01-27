import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DashboardPage: React.FC = () => {
  const [freelancers, setFreelancers] = useState<any[]>([]);

  useEffect(() => {
    // Aqui você faria uma requisição para buscar os freelancers do contratante
    axios.get('/api/freelancers') // Substitua com a URL correta da sua API
      .then(response => {
        setFreelancers(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar freelancers:', error);
      });
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard do Contratante</h1>
      <div className="mb-4">
        <button className="bg-blue-500 text-white p-2 rounded">Adicionar Freelancer</button>
      </div>
      <div className="space-y-4">
        {freelancers.map(freelancer => (
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