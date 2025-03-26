import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"

    repo = git.Repo(local_path)
    
    for tag in repo.tags:
        tag_obj = repo.tag(tag)
        print(f"\nTag: {tag}")
        
        if tag_obj.tag:
            print(f"Tag Message: {tag_obj.tag.message}")
            print(f"Tag Author: {tag_obj.tag.tagger}")
        else:
            print("Lightweight tag (no annotation)")

if __name__ == "__main__":
    main()
