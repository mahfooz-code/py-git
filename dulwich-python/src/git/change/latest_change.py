#!/usr/bin/python
# SPDX-License-Identifier: Apache-2.0 OR GPL-2.0-or-later

import sys
import time
from dulwich.repo import Repo

def get_last_change(repo_path, file_path):
    """Return the last commit that changed the given file."""
    repo = Repo(repo_path)
    path = file_path.encode("utf-8")
    walker = repo.get_walker(paths=[path], max_entries=1)
    try:
        commit = next(iter(walker)).commit
        return commit
    except StopIteration:
        return None

def print_last_change(repo_path, file_path):
    commit = get_last_change(repo_path, file_path)
    if commit is None:
        print(f"No file {file_path} anywhere in history.")
    else:
        print(
            f"{file_path} was last changed by {commit.author} at {time.ctime(commit.author_time)} (commit {commit.id})"
        )

def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} filename")
        sys.exit(1)
    repo_path = "."
    file_path = sys.argv[1]
    print_last_change(repo_path, file_path)

if __name__ == "__main__":
    main()