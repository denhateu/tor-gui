const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("electronAPI", {
   startProcess: () => ipcRenderer.invoke("start-process"),
   stopProcess: () => ipcRenderer.send("kill-process"),
   getLogs: () => ipcRenderer.invoke("get-logs"),
});

contextBridge.exposeInMainWorld("fileAPI", {
   readFile: (path) => ipcRenderer.invoke("read-file", path),
});
