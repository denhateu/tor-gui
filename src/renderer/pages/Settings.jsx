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

   useEffect(() => {
      saveConfig(config);
   }, [config]);

   async function saveConfig(newConfig) {
      await window.fileAPI.saveFile("./tor/torrc", newConfig);
      console.log("saved");
   }

   function handleConfigChange(value) {
      setConfig(value);
   }

   return (
      <div>
         <h1>Настройки</h1>
         <textarea value={config} onChange={(e) => handleConfigChange(e.target.value)} />
      </div>
   );
}
