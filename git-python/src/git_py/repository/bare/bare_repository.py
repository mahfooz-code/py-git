from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repo_path = Path(__file__).parents[5]
    # Repo object used to interact with Git repositories
    repo = Repo(repo_path)
    print(f"Is repo bare: {repo.bare}")
