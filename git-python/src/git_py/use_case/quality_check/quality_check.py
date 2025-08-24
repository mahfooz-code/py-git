import os

from git import Repo


def ci_pipeline(repo_path):
    repo = Repo(repo_path)
    origin = repo.remotes.origin

    # Pull latest changes
    origin.pull()

    # Run code quality checks (e.g., flake8)
    os.system("flake8 .")

    # If checks pass, continue with CI pipeline
    if os.system("flake8 .") == 0:
        print("Code quality checks passed!")
        # Continue with further CI steps
    else:
        print("Code quality checks failed!")


if __name__ == "__main__":
    repo_path = "/path/to/repo"
    ci_pipeline(repo_path)
