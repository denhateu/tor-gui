import React from "react";
import "../assets/css/style.css";

export default function App() {
   const startTorHandleClick = async () => {
      const result = await window.electronAPI.startProcess();
      console.log(result);
   }

   const stopTorHandleClick = async () => {
      const result = await window.electronAPI.stopProcess();
      console.log(result);
   }

   return (
      <div>
         <button onClick={startTorHandleClick}>Старт</button>
         <button onClick={stopTorHandleClick}>Стоп</button>
      </div>
   );
}