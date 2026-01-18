import React from "react";
import { HashRouter as Router, Routes, Route, Link } from 'react-router-dom';
import "../assets/css/style.css";
import HomePage from "./pages/Home";
import LogsPage from "./pages/Logs";
import SettingsPage from "./pages/Settings";

function App() {
   return (
      <Router>
         <nav>
            <Link to="/">Главная</Link>
            <Link to="/logs">Логи</Link>
            <Link to="/settings">Настройки</Link>
         </nav>
         <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/logs" element={<LogsPage />} />
            <Route path="/settings" element={<SettingsPage />} />
         </Routes>
      </Router>
   );
}

export default App;