import os
from pathlib import Path

import git


def main():
    repo_url = "git@github.com:mahfooz-code/spring-poc.git"
    repository_home = Path(os.environ["DATA_HOME"]) / "repository"
    local_path = repository_home / "my_local_repo"

    # Clone if the directory doesn't exist
    if not local_path.exists():
        repo = git.Repo.clone_from(repo_url, local_path)
        print("Repository cloned successfully!")
    else:
        repo = git.Repo(local_path)
        print("Repository already exists!")

    print(repo)


if __name__ == "__main__":
    main()
