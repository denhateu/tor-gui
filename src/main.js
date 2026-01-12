const { app, BrowserWindow, ipcMain } = require("electron");
const { spawn } = require("child_process");
const path = require("path");

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
   const child = spawn("./tor/tor/tor.exe", ["-f", "./tor/torrc"]);

   child.stdout.on("data", (data) => {
      console.log(data.toString("utf8"));
   });

   child.stderr.on("data", (data) => {
      console.log(data.toString("utf8"));
   });

   child.on("close", (code) => {
      console.log(`code: ${code}`);
   });

   return "process started";
});

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
   if (process.platform !== "darwin") app.quit();
});