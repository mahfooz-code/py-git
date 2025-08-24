import git

if __name__ == "__main__":
    # Load existing local repo
    my_repo = git.Repo("existing_repo")

    # Create a copy of the existing repo
    my_repo.clone("/path/to/clone_of_existing_repo")
