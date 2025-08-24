import os
from pathlib import Path

from git_py.util.git_util import (
    get_repo,
    get_tags,
    initialize_repository,
    print_tag_info,
)


def main():
    repository_path = Path(os.environ["DATA_HOME"]) / "repository" / "local_repo"
    initialize_repository(repository_path)
    repo = get_repo(repository_path)
    tags = get_tags(repo)

    for tag in tags:
        print_tag_info(repo, tag)


if __name__ == "__main__":
    main()
