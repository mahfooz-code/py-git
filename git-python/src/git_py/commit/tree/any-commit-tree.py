from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repo_path = Path(__file__).parents[5]

    # Repo object
    repo = Repo(repo_path)
    print(repo)

    prev_commits = list(repo.iter_commits(all=True, max_count=10))
    for commit in prev_commits:
        tree = commit.tree
        print(tree)
