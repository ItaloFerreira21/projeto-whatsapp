import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { getToken } from '../service.ts/authservice';

const ProtectedRoute: React.FC = () => {
  const token = getToken();
  console.log("Token usado na requisição:", token);
  

  return token ? <Outlet /> : <Navigate to="/login" />;
};

export default ProtectedRoute;