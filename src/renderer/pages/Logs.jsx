import React, { useEffect, useState } from "react";

export default function LogsPage() {
   const [logs, setLogs] = useState("");

   useEffect(() => {
      window.electronAPI.getLogs().then((history) => {
         setLogs(history.join('\n'));
      });
   }, []);

   return (
      <div>
         <h1>Логи</h1>
         <textarea value={logs} readOnly />
      </div>
   );
}