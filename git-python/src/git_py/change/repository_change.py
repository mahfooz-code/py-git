import os

from git import Repo

if __name__ == "__main__":
    # Check if a repo has changes
    repo = Repo(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        )
    )
    if repo.is_dirty(untracked_files=True):
        print("Changes detected.")
    else:
        print("No changes detected.")
