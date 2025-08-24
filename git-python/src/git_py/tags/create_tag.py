import os
from pathlib import Path

from git_py.util.git_util import get_repo, initialize_repository


def main():
    repository_path = Path(os.environ["DATA_HOME"]) / "repository" / "local_repo"
    initialize_repository(repository_path)
    repo = get_repo(repository_path)

    tag_name = "v2.0.0"
    repo.create_tag(tag_name, message="Release version 2.0.0")
    print(f"Tag {tag_name} created successfully!")


if __name__ == "__main__":
    main()
