#!/usr/bin/env python3
"""gito - git, but `gito "message"` does add + commit + push in one go.
Real git commands (status, pull, log, push...) are passed straight through to git."""
import subprocess
import sys


def git(*args):
    return subprocess.call(["git", *args])


def git_commands():
    """Names of git's own commands plus any aliases the user has set."""
    names = set()
    out = subprocess.run(["git", "help", "-a"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("   ") and line.strip():
            names.add(line.split()[0])
    cfg = subprocess.run(
        ["git", "config", "--get-regexp", r"^alias\."], capture_output=True, text=True
    ).stdout
    for line in cfg.splitlines():
        names.add(line.split()[0][len("alias."):])
    return names


def is_message(args):
    if not args:
        return False
    first = args[0]
    if first.startswith("-"):
        return False
    if any(c.isspace() for c in first):  # "fix the navbar" - clearly a message
        return True
    return first not in git_commands()  # one word: message unless it's a git command


def main():
    args = sys.argv[1:]

    if not is_message(args):
        sys.exit(git(*args))

    # gito "message" [extra args for git push...]
    message, extra = args[0], args[1:]

    if git("add", ".") != 0:
        sys.exit(1)

    # commit returns non-zero if there's nothing to commit - still try to push
    if git("commit", "-m", message) != 0:
        print("gito: commit failed or nothing to commit, pushing anyway...")

    sys.exit(git("push", *extra))


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print("gito: git not found - is it installed and on your PATH?")
        sys.exit(1)
