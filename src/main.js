const { app, BrowserWindow, ipcMain } = require("electron");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");
const kill = require('tree-kill');

let mainWindow = null;
let torProcess = null
let logsList = [];

function createWindow() {
   mainWindow = new BrowserWindow({
      width: 640,
      height: 480,
      webPreferences: {
         preload: path.join(__dirname, "preload.js"),
         contextIsolation: true,
      }
   });

   mainWindow.loadFile("public/index.html");
}

function onLog(log) {
   logsList.push(log);
   if (mainWindow) {
      mainWindow.webContents.send("log-message", log);
   }
}

ipcMain.handle("start-process", () => {
   torProcess = spawn("./tor/tor/tor.exe", ["-f", "./tor/torrc"]);

   torProcess.stdout.on("data", (data) => {
      let dataString = data.toString("utf8");

      onLog(dataString);
      console.log(dataString);
   });

   torProcess.stderr.on("data", (data) => {
      let dataString = data.toString("utf8");

      onLog(`Errro: ${dataString}`);
      console.log(dataString);
   });

   torProcess.on("close", (code) => {
      onLog(`Code: ${code}`);
      console.log(`code: ${code}`);
   });

   return true;
});

ipcMain.on("kill-process", () => {
   if (torProcess !== null) {
      kill(torProcess.pid, "SIGKILL", (err) => {
         if (err) {
            console.log(`Failed to kill process: ${err}`);
            return false;
         } else {
            console.log("Process killed successfully!");
            torProcess = null;
         }
      });

      return true;
   } else {
      return false;
   }
});

ipcMain.handle("get-logs", () => logsList);

ipcMain.handle("read-file", async (_, filePath) => {
   return fs.readFileSync(filePath, "utf-8");
});

ipcMain.handle("save-file", async (_, { filePath, content }) => {
   fs.writeFileSync(filePath, content, "utf-8");
   return true;
});

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
   if (process.platform !== "darwin") app.quit();
});