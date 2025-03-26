import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"
    
    new_branch = "feature-branch"
    repo = git.Repo(local_path)
    
    # Create a new branch if it doesn't exist
    if new_branch not in repo.heads:
        repo.git.checkout("-b", new_branch)  # Create and switch to the branch
        print(f"Switched to new branch: {new_branch}")
    else:
        repo.git.checkout(new_branch)  # Switch to the branch
        print(f"Switched to existing branch: {new_branch}")

if __name__ == "__main__":
    main()
