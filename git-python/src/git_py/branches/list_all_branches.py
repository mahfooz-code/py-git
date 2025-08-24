import os
from pathlib import Path

import git

if __name__ == "__main__":
    repository_home = Path(os.environ["DATA_HOME"]) / "repository"
    repo = git.Repo.init(repository_home / "my_local_repo")

    # List all branches
    print("Listing all branches:")
    for branch in repo.branches:
        print(f"\t{branch}")

    # Create a new branch
    try:
        repo.git.branch("my_new_branch")
    except git.exc.GitCommandError as error:
        print(error)

    # List all branches again
    print("Listing all branches again:")
    for branch in repo.branches:
        print(f"\t{branch}")

    # To check out master again:
    repo.git.checkout("master")

    # List all branches again
    print("Listing all branches after checkout:")
    for branch in repo.branches:
        print(f"\t{branch}")

    # Delete the new branch
    repo.git.branch("-D", "my_new_branch")

    # List all branches again
    print("Listing all branches after delete:")
    for branch in repo.branches:
        print(f"\t{branch}")
