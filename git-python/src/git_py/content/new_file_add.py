import os
from pathlib import Path

from git_py.util.git_util import (
    commit_changes,
    create_file,
    get_repo,
    push_changes,
    stage_file,
)


def main():
    repository_home = Path(os.environ["DATA_HOME"]) / "repository"
    local_path = repository_home / "content_repo"
    file_path = local_path / "new_file.txt"
    file_content = "Hello, GitPython!\n"
    commit_message = "Added a new file using GitPython"
    remote_branch = "main_new"

    repo = get_repo(local_path)
    create_file(file_path, file_content)
    stage_file(repo, file_path)
    commit_changes(repo, commit_message)
    push_changes(repo, remote_branch)


if __name__ == "__main__":
    main()
