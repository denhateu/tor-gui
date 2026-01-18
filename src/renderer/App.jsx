import React from "react";
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from "./pages/Home";
import LogsPage from "./pages/Logs";
import SettingsPage from "./pages/Settings";

function App() {
   return (
      <Router>
         <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/logs" element={<LogsPage />} />
            <Route path="/settings" element={<SettingsPage />} />
         </Routes>
      </Router>
   );
}

export default App;