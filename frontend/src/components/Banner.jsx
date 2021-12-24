import React from 'react';
import { Link } from 'react-router-dom';

const Banner = () => {
  return (
    <div className="alert alert-dismissible alert-secondary">
      <strong>
        <i className="fas fa-lightbulb"></i>
        {'  '}¿Quieres ver más productos?
      </strong>
      {'  '}Puedes hacer{' '}
      <Link to="recomendaciones" className="alert-link">
        click aquí
      </Link>{' '}
      para ver algunas recomendaciones
    </div>
  );
};

export default Banner;
