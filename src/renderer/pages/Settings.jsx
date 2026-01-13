import React, { useState, useEffect } from "react";

export default function SettingsPage() {
   const [config, setConfig] = useState("");

   useEffect(() => {
      async function loadConfig() {
         const data = await window.fileAPI.readFile("./tor/torrc");
         setConfig(data);
      }

      loadConfig();
   }, []);

   return (
      <div>
         <h1>Настройки</h1>
         <textarea value={config} readOnly />
      </div>
   );
}
