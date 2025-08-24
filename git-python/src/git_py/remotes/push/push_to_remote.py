import os
from pathlib import Path

from git_py.util.git_util import get_repo, initialize_repository

if __name__ == "__main__":
    repository_path = Path(os.environ["DATA_HOME"]) / "repository" / "local_repo"
    initialize_repository(repository_path)
    repo = get_repo(repository_path)

    # List remotes
    print("Remotes:")
    for remote in repo.remotes:
        print(f"- {remote.name} {remote.url}")

    print("Push changes:")
    for push in repo.remotes.origin.push():
        print(push.summary)
