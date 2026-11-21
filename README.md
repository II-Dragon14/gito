# gito
   > **Note:** To see a nicer polished version of these instructions, follow this [link](https://ilan.bloxxer.dev/gito).

   >  *Also, if you have time, please visit my [main site](https://ilan.bloxxer.dev). It really helps.*

It's just git, except `gito "message"` does **add, commit and push** in one go. Everything else is passed straight through to git.

```
git add .
git commit -m "message"        becomes        gito "message"
git push
```

Made for Windows, but the Python script runs anywhere Python and git do.

---

## Contents

- [Requirements](#requirements)
- [Install (the .exe)](#install-the-exe)
- [Add gito to your PATH](#add-gito-to-your-path)
- [Check it works](#check-it-works)
- [Usage](#usage)
- [How gito tells a message from a command](#how-gito-tells-a-message-from-a-command)
- [Good to know](#good-to-know)
- [Build the .exe yourself](#build-the-exe-yourself)
- [Run it without building](#run-it-without-building)
- [Troubleshooting](#troubleshooting)

---

## Requirements

- **Git** installed. If `git --version` works in a terminal, you're set. Otherwise install Git for Windows from [git-scm.com](https://git-scm.com).
- You do **not** need Python to run the `.exe`. You only need it if you want to run `gito.py` directly or build the exe yourself.

---

## Install (the .exe)

1. Download `gito.exe` from the [latest release](https://github.com/II-Dragon14/gito/releases/latest).
2. Put it in a folder of its own, for example `C:\Tools\gito`.
3. Windows may warn about the download because the file isn't code-signed. If you trust it, choose **More info**, then **Run anyway**.
4. Add that folder to your PATH (next section).

---

## Add gito to your PATH

Adding the folder to your PATH lets you type `gito` in any folder, in any terminal. Add the **folder** (`C:\Tools\gito`), not the exe itself.

### Option A: Windows settings

1. Press the Windows key and type `environment variables`.
2. Open **Edit environment variables for your account**.
3. Under **User variables**, select **Path** and click **Edit**.
4. Click **New** and paste `C:\Tools\gito`.
5. Click **OK** on every window.

### Option B: one line in PowerShell

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path","User") + ";C:\Tools\gito", "User")
```

This only changes your own account and doesn't need administrator rights. If your folder is somewhere else, change the path in the line above.

---

## Check it works

Open a **new** terminal (one that was already open won't see the change) and run:

```
gito --version
```

You should see your git version, for example `git version 2.x`. That's gito passing the command through to git.

If Windows says `gito` isn't recognised, the folder isn't on your PATH yet. Check the path you added and reopen the terminal.

---

## Usage

Open a terminal in your project folder (it must already be a git repository) and run:

```
gito "fix the login button"
```

gito stages everything, commits it with that message, and pushes it.

| Command | What it does |
| --- | --- |
| `gito "your message"` | Runs `git add .`, `git commit -m "your message"`, then `git push`. |
| `gito "your message" origin main` | Anything after the message is handed to `git push`. Here it pushes to `origin main`. |
| `gito "first commit" -u origin main` | Useful for the first push of a new branch, because `-u` remembers where it goes next time. |
| `gito status` | Any real git command goes straight to git. The same goes for `gito pull`, `gito push`, `gito log --oneline`, `gito checkout -b new-branch` and the rest. |

### Starting a brand new repository

```
cd C:\path\to\folder
git init
git remote add origin <your-repo-url>
gito "first commit" -u origin main
```

---

## How gito tells a message from a command

- If the first thing you type is a **git command** (including any aliases you've set up) or starts with `-`, it goes to git untouched.
- Anything else is treated as a **commit message**.
- If the first argument contains a space, such as `"fix the navbar"`, it is always treated as a message.

---

## Good to know

- **Use quotes around your message.** Without them, only the first word counts as the message and the rest is handed to `git push`.
- **It stages everything.** `gito "message"` runs `git add .`, which includes new files. Check `gito status` first if you're unsure, and keep a `.gitignore` for files that must stay private, such as keys and passwords.
- **Nothing new to commit?** It tells you, then pushes anyway. That's handy for pushing a commit you made earlier.
- **If staging fails, it stops.** Nothing is committed or pushed.
- **One-word clashes.** A one-word message that is also a git command, such as `status`, goes to git. Make it two words.
- **"git not found"** means Git isn't installed or isn't on your PATH.

---

## Build the .exe yourself

```
pip install pyinstaller
pyinstaller --onefile gito.py
```

The exe appears in the `dist` folder as `gito.exe`. Then follow the install steps above.

- **Don't use `--noconsole`.** gito is a command-line tool and needs a console to show git's output.
- `--onefile` starts slightly slower because it unpacks itself on each run. Leave it out and keep the whole `dist\gito` folder if that bothers you.
- Antivirus programs sometimes flag PyInstaller exes as suspicious. It's a false positive, but you may need to add an exclusion.
- The `build` folder and `gito.spec` file it creates are safe to delete.
- If you edit `gito.py`, rebuild the exe to pick up the changes.

---

## Run it without building

If you have Python, you can skip the exe entirely.

1. Put `gito.py` and `gito.cmd` in a folder on your PATH, for example `C:\Tools\gito`.
2. `gito.cmd` is a one-line launcher that lets you type `gito` instead of `python gito.py`:

   ```bat
   @echo off
   python "%~dp0gito.py" %*
   ```

3. Edits to `gito.py` take effect straight away, with nothing to rebuild.

On macOS or Linux, run `chmod +x gito.py` and symlink it somewhere on your PATH as `gito`.

---

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `gito` is not recognised | The folder isn't on your PATH, or the terminal was open before you changed it. Check the path and open a new terminal. |
| `fatal: not a git repository` | That message comes from git. You're in a folder that isn't a repo. `cd` into your project, or run `git init` first. |
| `git not found` | Install Git and make sure `git --version` works in a terminal. |
| Windows warns about the download | The exe isn't code-signed. Choose **More info**, then **Run anyway**. |
| Antivirus flags the exe | Common false positive with PyInstaller. Add an exclusion, or run `gito.py` directly instead. |
| `gito fix navbar` fails | Put the message in quotes: `gito "fix navbar"`. |
| `gito status` isn't treated as a message | Working as intended. `status` is a git command, so it goes to git. |
