import os

from git import Repo


def ci_pipeline(repo_path):
    repo = Repo(repo_path)
    origin = repo.remotes.origin

    # Pull latest changes
    origin.pull()

    # Generate documentation (assuming a script generates docs)
    os.system("generate_docs")

    # Add and commit the changes
    repo.index.add(["docs"])
    repo.index.commit("Auto-update documentation")

    # Push changes
    origin.push()


if __name__ == "__main__":
    repo_path = "/path/to/repo"
    ci_pipeline(repo_path)
