import os

from git import Repo


def ci_pipeline(repo_path):
    repo = Repo(repo_path)
    origin = repo.remotes.origin

    # Pull latest changes
    origin.pull()

    # Run tests (assuming tests are run via a script)
    os.system("python -m unittest discover")

    # If tests pass, deploy
    if os.system("python -m unittest discover") == 0:
        print("Tests passed! Deploying...")
        # Deployment logic here
        # For example, push to a production server
        origin.push()
    else:
        print("Tests failed! Deployment aborted.")


if __name__ == "__main__":
    repo_path = "/path/to/repo"
    ci_pipeline(repo_path)
