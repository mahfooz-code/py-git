import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    repo_path = f"{reposutory_home}/my_local_repo"
    
    repo = git.Repo(repo_path)

    # Get all tags
    tags = repo.tags
    print("Available Tags:")
    for tag in tags:
        print(tag)
        
if __name__ == "__main__":
    main()
