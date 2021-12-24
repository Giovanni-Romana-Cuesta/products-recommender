import React, { useEffect, useState } from 'react';
import Banner from '../components/Banner';

const Compras = () => {
  const url = 'http://localhost:4000/orders/123456789';
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
        <i className="fas fa-shopping-bag"></i>Mis compras
      </h2>
      <Banner />
      {!data
        ? 'Cargando...'
        : data.orders.map((item) => {
            return (
              <div className="card border-light mb-3" key={item.orderID}>
                <div className="card-header">
                  <i class="fas fa-tags"></i>Compra:{'  '}#{item.orderID}
                </div>
                <div className="card-body">
                  <h4 className="card-title">Detalles</h4>
                  <p className="card-text">
                    <span className="fw-bold">Fecha: </span> {item.date}
                  </p>
                  <p className="card-text">
                    <span className="fw-bold">Valor compra: </span>${item.value}
                  </p>
                  <table className="table table-hover">
                    <thead>
                      <tr>
                        <th scope="col">Artículo</th>
                        <th scope="col">Valor</th>
                      </tr>
                    </thead>
                    <tbody>
                      {item.products.map((products) => {
                        return (
                          <tr className="table-active">
                            <th scope="row">{products.name}</th>
                            <td>${products.price}</td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>
            );
          })}
    </div>
  );
};

export default Compras;
