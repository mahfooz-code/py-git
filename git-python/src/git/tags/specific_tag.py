import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"

    repo = git.Repo(local_path)
    
    tag_name = "v2.0.0"  # Change to your desired tag

    # Get the tag reference
    tag = repo.tags[tag_name]

    # Get commit details associated with the tag
    commit = tag.commit
    print(f"Tag: {tag_name}")
    print(f"Commit Hash: {commit.hexsha}")
    print(f"Commit Message: {commit.message}")
    print(f"Author: {commit.author.name} <{commit.author.email}>")
    print(f"Date: {commit.committed_datetime}")

if __name__ == "__main__":
    main()
