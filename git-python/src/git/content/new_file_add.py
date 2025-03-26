import os,git

def main():
    reposutory_home = os.environ['DATA_HOME'].replace("\\", "/") + "/repository"
    local_path = f"{reposutory_home}/my_local_repo"
    
    repo = git.Repo(local_path)
    
    file_path = os.path.join(local_path, "new_file.txt")

    # Write to the file
    with open(file_path, "w") as file:
        file.write("Hello, GitPython!\n")

    print("File created successfully!")
    
    ##  Stage the File
    repo.index.add([file_path])
    print("File added to staging area!")
    
    repo.index.commit("Added a new file using GitPython")
    print("Changes committed successfully!")

    origin = repo.remote(name="origin")
    origin.push(new_branch)
    print(f"Changes pushed to remote branch: {new_branch}")


if __name__ == "__main__":
    main()
