const { app, BrowserWindow, ipcMain } = require("electron");
const { spawn } = require("child_process");
const path = require("path");
const kill = require('tree-kill');

let torProcess = null

function createWindow() {
   const win = new BrowserWindow({
      width: 640,
      height: 480,
      webPreferences: {
         preload: path.join(__dirname, "preload.js"),
         contextIsolation: true,
      }
   });

   win.loadFile("public/index.html");
}

ipcMain.handle("start-process", () => {
   torProcess = spawn("./tor/tor/tor.exe", ["-f", "./tor/torrc"]);

   torProcess.stdout.on("data", (data) => {
      console.log(data.toString("utf8"));
   });

   torProcess.stderr.on("data", (data) => {
      console.log(data.toString("utf8"));
   });

   torProcess.on("close", (code) => {
      console.log(`code: ${code}`);
   });

   return "process started";
});

ipcMain.on("kill-process", () => {
   if (torProcess !== null) {
      kill(torProcess.pid, "SIGKILL", (err) => {
         if (err) {
            console.log(`Failed to kill process: ${err}`);
         } else {
            console.log("Process killed successfully!");
            torProcess = null;
         }
      });
   }
});

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
   if (process.platform !== "darwin") app.quit();
});