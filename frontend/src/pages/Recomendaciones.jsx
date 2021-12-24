import React, { useEffect, useState } from 'react';
import '../styles/styles.css';

const Recomendaciones = () => {
  const url = 'http://localhost:4000/recommendations/987456321';
  const [data, setData] = useState();

  const fetchApi = async () => {
    const response = await fetch(url);
    const responseJSON = await response.json();
    setData(responseJSON[0]);
  };

  useEffect(() => {
    fetchApi();
  }, []);

  return (
    <div className="p-4">
      <h2>
        <i className="fas fa-lightbulb"></i>Recomendaciones
      </h2>
      <main className="products-container">
        {!data
          ? 'Cargando...'
          : data.recomendaciones.map((product) => {
              return (
                <>
                  <div class="card mb-3">
                    <div class="card-body">
                      <h5 class="card-title">{product.name}</h5>
                    </div>
                    <img className="card-image" src={product.image} alt="" />
                    <div class="card-body">
                      <p class="card-text">
                        <span class="badge bg-light">{product.brand}</span>
                      </p>
                      <p className="card-text">
                        <p class="text-primary">Precio: ${product.price}</p>
                      </p>
                    </div>
                  </div>
                </>
              );
            })}
      </main>
    </div>
  );
};

export default Recomendaciones;
