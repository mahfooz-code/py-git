import os
from pathlib import Path

from git_py.util.git_util import get_repo, initialize_repository


def main():
    repository_path = Path(os.environ["DATA_HOME"]) / "repository" / "local_repo"
    initialize_repository(repository_path)
    repo = get_repo(repository_path)
    tag_name = "v2.0.0"
    repo.remotes.origin.push(tag_name)
    print(f"Tag {tag_name} pushed to remote!")


if __name__ == "__main__":
    main()
