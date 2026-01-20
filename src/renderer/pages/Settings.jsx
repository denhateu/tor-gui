import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import Header from "../components/Header";
import Container from "../components/Container";

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
      <>
         <Header>
            <nav className="flex items-center space-x-2 py-4">
               <Link to="/">
                  <div className="button">
                     <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" className="w-6 h-6 bi bi-arrow-left" viewBox="0 0 16 16">
                        <path fillRule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
                     </svg>
                  </div>
               </Link>
            </nav>
         </Header>
         <main className="flex-1">
            <section className="pt-[80px]">
               <Container>
                  <h1 className="text-4xl font-bold mb-2">Настройки</h1>
                  <textarea value={config} onChange={(e) => handleConfigChange(e.target.value)} className="textarea w-full min-h-[200px] resize-vertical" />
               </Container>
            </section>
         </main>
      </>
   );
}
