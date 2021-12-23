import React from 'react';
import { Link } from 'react-router-dom';

/* 
 todo: fijar barra de navegacion en el top de la app
 */
const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary p-3">
      <div className="container-fluid">
        <a className="navbar-brand fs-3 fw-bold">RECOMENDAPP</a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarColor01"
          aria-controls="navbarColor01"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarColor01">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <Link to="/" className="link nav-link">
                <i className="fas fa-shopping-bag"></i> Mis compras
              </Link>
            </li>
            <li className="nav-item">
              <Link to="recomendaciones" className="link nav-link">
                <i className="fas fa-lightbulb"></i> Recomendaciones
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
