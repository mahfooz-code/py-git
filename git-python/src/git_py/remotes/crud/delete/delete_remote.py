import os

import git

if __name__ == "__main__":
    repository_folder = "git-python-lib"
    repository_path = os.environ["DATA_HOME"].replace("\\", "/") + "/repository"
    repository_dir = repository_path + "/" + repository_folder

    repo = git.Repo(repository_dir)

    # List remotes
    print("Remotes:")
    for remote in repo.remotes:
        print(f"- {remote.name} {remote.url}")

    # Delete a remote
    # repo.delete_remote("origin2")

    # List remotes
    print("Remotes:")
    for remote in repo.remotes:
        print(f"- {remote.name} {remote.url}")
