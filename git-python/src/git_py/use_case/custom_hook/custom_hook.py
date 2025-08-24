import os

from git import Repo


# Function to create a pre-commit hook
def create_pre_commit_hook(repo_path):
    # Open the Git repository
    repo = Repo(repo_path)
    hooks_dir = os.path.join(repo.git_dir, "hooks")
    hook_path = os.path.join(hooks_dir, "pre-commit")

    # Hook content to run tests
    hook_content = """#!/bin/sh
    # Run tests
    python -m unittest discover

    # Check the exit status of the tests
    if [ $? -ne 0 ]; then
        echo "Tests failed. Aborting commit."
        exit 1
    fi

    echo "All tests passed. Proceeding with commit."
    exit 0
    """

    # Create the pre-commit hook file
    with open(hook_path, "w") as hook_file:
        hook_file.write(hook_content)

    # Make the hook executable
    os.chmod(hook_path, 0o775)

    print(f"Pre-commit hook created at {hook_path}")


# Function to create a post-commit hook
def create_post_commit_hook(repo_path):
    # Open the Git repository
    repo = Repo(repo_path)
    hooks_dir = os.path.join(repo.git_dir, "hooks")
    hook_path = os.path.join(hooks_dir, "post-commit")

    # Hook content to push changes
    hook_content = """#!/bin/sh
    # Push changes to remote
    git push origin $(git rev-parse --abbrev-ref HEAD)
    """

    # Create the post-commit hook file
    with open(hook_path, "w") as hook_file:
        hook_file.write(hook_content)

    # Make the hook executable
    os.chmod(hook_path, 0o775)

    print(f"Post-commit hook created at {hook_path}")


if __name__ == "__main__":
    # Path to your repository
    repo_path = "/path/to/your/repo"

    # Create the pre-commit hook
    create_pre_commit_hook(repo_path)

    # Create the post-commit hook
    create_post_commit_hook(repo_path)
