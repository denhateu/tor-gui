const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("electronAPI", {
   startProcess: () => ipcRenderer.invoke("start-process"),
   stopProcess: () => ipcRenderer.send("kill-process"),
});