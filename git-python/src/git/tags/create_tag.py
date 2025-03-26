import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"

    tag_name = "v2.0.0"
    repo = git.Repo(local_path)
    repo.create_tag(tag_name, message="Release version 2.0.0")
    print(f"Tag {tag_name} created successfully!")

if __name__ == "__main__":
    main()
