# gito
What it does

Normally, saving your work to GitHub takes three commands. With gito it's one.
git add .
then
git commit -m "message"
then
git push

becomes
Copy
gito push "message"

Any other command, such as gito status or gito pull, goes to git exactly as you typed it.
2
Install and add it to your PATH

Adding gito to your PATH lets you type gito in any folder, in any terminal.

Install Git first. If git --version already works in a terminal, skip this. Otherwise install Git for Windows from git-scm.com.
    Download gito.exe and put it in a folder of its own. Get it from the latest release on GitHub (use the button at the top of this page), then save it somewhere like C:\Tools\gito. Windows may warn about the download because the file isn't code-signed. If you trust it, choose More info, then Run anyway.
    Add that folder to your PATH. Pick one of these:
    Option A: in Windows settings

Press Win and type environment variables, then open Edit environment variables for your account. Under User variables select Path, click Edit, then New, and paste C:\Tools\gito. Click OK on every window.
    Option B: one line in PowerShell
    [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path","User") + ";C:\Tools\gito", "User")

This changes only your own account and doesn't need administrator rights. If your folder is somewhere else, change the path in the line above.
    Open a new terminal and check it works. A terminal that was already open won't see the change.
    Copy
    gito --version

You should see your Git version, for example git version 2.x. That's gito passing the command through to git. If Windows says gito isn't recognised, the folder isn't on your PATH yet, so check the path you added and reopen the terminal.

3
How to use it

Open a terminal in your project folder, the one that's already a git repository, and run:
Copy
gito push "fix the login button"

Put your message in quotes. gito then stages everything, commits it with that message and pushes it.
gito push "your message"
Runs git add ., git commit -m "your message", then git push.
gito push "your message" origin main
Anything after the message is handed to git push. Here it pushes to origin main.
gito push "first commit" -u origin main
Useful for the first push of a new branch, because -u remembers where it goes next time.
gito status
Any command that isn't push goes straight to git. The same goes for gito pull, gito log --oneline, gito checkout -b new-branch and the rest.
4
Good to know

A few things that behave in ways you might not expect.

    It stages everything. gito push runs git add ., which includes new files. Check gito status first if you're unsure, and keep a .gitignore for files that must stay private, such as keys and passwords.
    Nothing new to commit? It tells you, then pushes anyway. That's handy for pushing a commit you made earlier.
    If staging fails, it stops and nothing is committed or pushed.
    You must give a message. gito push on its own just shows the usage line.
    Only the word push is special. Every other command behaves exactly as it does in git.
    "git not found" means Git isn't installed or isn't on your PATH.

What it does

Normally, saving your work to GitHub takes three commands. With gito it's one.
git add .
then
git commit -m "message"
then
git push

becomes
Copy
gito push "message"

Any other command, such as gito status or gito pull, goes to git exactly as you typed it.
2
Install and add it to your PATH

Adding gito to your PATH lets you type gito in any folder, in any terminal.

    Install Git first. If git --version already works in a terminal, skip this. Otherwise install Git for Windows from git-scm.com.
    Download gito.exe and put it in a folder of its own. Get it from the latest release on GitHub (use the button at the top of this page), then save it somewhere like C:\Tools\gito. Windows may warn about the download because the file isn't code-signed. If you trust it, choose More info, then Run anyway.
    Add that folder to your PATH. Pick one of these:
    Option A: in Windows settings

    Press Win and type environment variables, then open Edit environment variables for your account. Under User variables select Path, click Edit, then New, and paste C:\Tools\gito. Click OK on every window.
    Option B: one line in PowerShell
    Copy
    [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path","User") + ";C:\Tools\gito", "User")

    This changes only your own account and doesn't need administrator rights. If your folder is somewhere else, change the path in the line above.
    Open a new terminal and check it works. A terminal that was already open won't see the change.
    Copy
    gito --version

    You should see your Git version, for example git version 2.x. That's gito passing the command through to git. If Windows says gito isn't recognised, the folder isn't on your PATH yet, so check the path you added and reopen the terminal.

3
How to use it

Open a terminal in your project folder, the one that's already a git repository, and run:
Copy
gito push "fix the login button"

Put your message in quotes. gito then stages everything, commits it with that message and pushes it.
gito push "your message"
Runs git add ., git commit -m "your message", then git push.
gito push "your message" origin main
Anything after the message is handed to git push. Here it pushes to origin main.
gito push "first commit" -u origin main
Useful for the first push of a new branch, because -u remembers where it goes next time.
gito status
Any command that isn't push goes straight to git. The same goes for gito pull, gito log --oneline, gito checkout -b new-branch and the rest.
4
Good to know

A few things that behave in ways you might not expect.

    It stages everything. gito push runs git add ., which includes new files. Check gito status first if you're unsure, and keep a .gitignore for files that must stay private, such as keys and passwords.
    Nothing new to commit? It tells you, then pushes anyway. That's handy for pushing a commit you made earlier.
    If staging fails, it stops and nothing is committed or pushed.
    You must give a message. gito push on its own just shows the usage line.
    Only the word push is special. Every other command behaves exactly as it does in git.
    "git not found" means Git isn't installed or isn't on your PATH.

