import os,git

def main():
    repo_url = "git@github.com:mahfooz-code/spring-poc.git"
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"
    
    # Clone if the directory doesn't exist
    if not os.path.exists(local_path):
        repo = git.Repo.clone_from(repo_url, local_path)
        print("Repository cloned successfully!")
    else:
        repo = git.Repo(local_path)
        print("Repository already exists!")

if __name__ == "__main__":
    main()
