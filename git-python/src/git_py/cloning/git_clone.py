import os
from pathlib import Path

from git import Repo


def main():
    repository_folder = "JavaPro"
    repository_path = Path(os.environ["DATA_HOME"]) / "repository"
    local_dir = repository_path / repository_folder

    Repo.clone_from("https://github.com/official-himanshu/JavaPro.git", local_dir)

    # Open an existing local repo
    repo = Repo(local_dir)
    print(repo)


if __name__ == "__main__":
    main()
