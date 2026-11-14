#!/usr/bin/env python3
"""gito - git, but `gito push "message"` does add + commit + push in one go.
Every other command is passed straight through to git."""
import subprocess
import sys


def git(*args):
    return subprocess.call(["git", *args])


def main():
    args = sys.argv[1:]

    if not args or args[0] != "push":
        sys.exit(git(*args))

    # gito push "message" [extra args for git push...]
    if len(args) < 2:
        print('Usage: gito push "commit message"')
        sys.exit(1)

    message, extra = args[1], args[2:]

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
