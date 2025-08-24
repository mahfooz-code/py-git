import git

if __name__ == "__main__":
    # Check out via HTTPS
    git.Repo.clone_from("https://github.com/DevDungeon/Cookbook", "Cookbook-https")

    # or clone via ssh (will use default keys)
    git.Repo.clone_from("git@github.com:DevDungeon/Cookbook", "Cookbook-ssh")
