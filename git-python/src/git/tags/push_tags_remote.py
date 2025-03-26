import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"

    repo = git.Repo(local_path)
    tag_name = "v2.0.0"
    repo.remotes.origin.push(tag_name)
    print(f"Tag {tag_name} pushed to remote!")

if __name__ == "__main__":
    main()
