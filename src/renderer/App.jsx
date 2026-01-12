import React from "react";
import "../assets/css/style.css";

export default function App() {
   const startTorHandleClick = async () => {
      const result = await window.electronAPI.startProcess();
      console.log(result);
   }

   return (
      <button onClick={startTorHandleClick}>Старт</button>
   );
}