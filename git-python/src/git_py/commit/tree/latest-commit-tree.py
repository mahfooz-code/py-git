import os

from git import Repo

if __name__ == "__main__":
    repo_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        )
    )
    # Repo object used to interact with Git repositories
    repo = Repo(repo_path)

    latest_commit_tree = repo.head.commit.tree

    print(latest_commit_tree.list_traverse())
