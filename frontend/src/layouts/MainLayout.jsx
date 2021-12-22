import React from 'react';
import '../styles/mainlayout.css';
import Navbar from '../components/Navbar';
import { Outlet } from 'react-router-dom';

const MainLayout = () => {
  return (
    <div className="main-layout">
      <Navbar />
      <Outlet />
    </div>
  );
};

export default MainLayout;
