from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repo = Repo(Path(__file__).parents[3])
    assert repo.head.is_valid(), "Not a valid head"
    tree = repo.head.commit.tree
    print(tree.commit_id)
