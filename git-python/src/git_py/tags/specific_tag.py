import os
from pathlib import Path

from git_py.util.git_util import get_repo, initialize_repository


def main():
    repository_path = Path(os.environ["DATA_HOME"]) / "repository" / "local_repo"
    initialize_repository(repository_path)
    repo = get_repo(repository_path)
    tag_name = "v2.0.0"

    # Get the tag reference
    tag = repo.tags[tag_name]

    # Get commit details associated with the tag
    commit = tag.commit
    print(f"Tag: {tag_name}")
    print(f"Commit Hash: {commit.hexsha}")
    print(f"Commit Message: {commit.message}")
    print(f"Author: {commit.author.name} <{commit.author.email}>")
    print(f"Date: {commit.committed_datetime}")


if __name__ == "__main__":
    main()
