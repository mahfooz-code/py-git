import git

if __name__ == "__main__":
    repo = git.Repo("my_repo")

    # Provide a list of the files to stage
    repo.index.add([".gitignore", "README.md"])

    # Provide a commit message
    repo.index.commit("Initial commit.")
