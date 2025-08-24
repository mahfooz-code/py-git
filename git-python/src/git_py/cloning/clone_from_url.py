import os
from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repository_folder = "quick-start-tutorial-files"
    repository_path = Path(os.environ["DATA_HOME"]) / "repository"
    local_dir = repository_path / repository_folder

    repo_url = "https://github.com/gitpython-developers/QuickStartTutorialFiles.git"

    repo = Repo.clone_from(repo_url, local_dir)
    for remote in repo.remotes:
        print(remote.name, remote.url)
