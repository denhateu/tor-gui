import React from "react";
import { HashRouter as Router, Routes, Route, Link } from 'react-router-dom';
import "../assets/css/null.css";
import HomePage from "./pages/Home";
import LogsPage from "./pages/Logs";

function App() {
   return (
      <Router>
         <nav>
            <Link to="/">Главная</Link>
            <Link to="/logs">Логи</Link>
         </nav>
         <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/logs" element={<LogsPage />} />
         </Routes>
      </Router>
   );
}

export default App;