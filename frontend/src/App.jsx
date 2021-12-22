import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './layouts/MainLayout';
import Compras from './pages/Compras';
import Recomendaciones from './pages/Recomendaciones';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route path="/" element={<Compras />} />
          <Route path="recomendaciones" element={<Recomendaciones />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
