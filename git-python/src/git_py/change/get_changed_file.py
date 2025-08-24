import os

from git import Repo

if __name__ == "__main__":
    # Get a diff of file changes
    repo = Repo(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        )
    )

    # Check differences between current files and last commit
    diff = repo.git.diff("--name-only")
    print(diff)
