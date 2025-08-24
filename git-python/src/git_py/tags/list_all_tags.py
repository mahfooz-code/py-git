import os
from pathlib import Path

from git_py.util.git_util import get_repo, initialize_repository


def main():
    repository_path = Path(os.environ["DATA_HOME"]) / "repository" / "local_repo"
    initialize_repository(repository_path)
    repo = get_repo(repository_path)

    # Get all tags
    tags = repo.tags
    print("Available Tags:")
    for tag in tags:
        print(tag)


if __name__ == "__main__":
    main()
