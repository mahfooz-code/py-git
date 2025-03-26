import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"

    repo = git.Repo(local_path)
    tag_name = "v2.0.0"  # Change this to your tag
    repo.git.checkout(tag_name)
    print(f"Checked out tag: {tag_name}")

if __name__ == "__main__":
    main()
