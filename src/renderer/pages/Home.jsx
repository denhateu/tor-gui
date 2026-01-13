import React from "react";

export default function HomePage() {
   const startTorHandleClick = async () => {
      const result = await window.electronAPI.startProcess();
   }

   const stopTorHandleClick = async () => {
      const result = await window.electronAPI.stopProcess();
   }

   return (
      <div>
         <button onClick={startTorHandleClick}>Старт</button>
         <button onClick={stopTorHandleClick}>Стоп</button>
      </div>
   );
}