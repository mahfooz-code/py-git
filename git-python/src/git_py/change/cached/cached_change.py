from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repository_path = Path(__file__).parents[5]
    print(f"repository path: {repository_path}")

    # Get a diff of file changes
    repo = Repo(repository_path)
    # Check differences between current files and last commit
    diff = repo.git.diff("--cached")
    print(diff)
