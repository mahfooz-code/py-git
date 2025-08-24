import os

from git import Repo

if __name__ == "__main__":
    repository_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        )
    )
    print(f"repository path: {repository_path}")

    # Get a diff of file changes
    repo = Repo(repository_path)

    # Check differences between current files and last commit

    diff = repo.git.diff(repo.head.commit.tree)
    print(diff)
