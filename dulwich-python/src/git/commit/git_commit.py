from git.util.git_util import (
    add_blob_to_repo,
    create_commit,
    create_file,
    create_repo_dir,
    create_tree,
    get_repo_dir,
    initialize_repo,
    update_refs_and_index,
)


def main():
    repo_dir = get_repo_dir("deluwich")
    create_repo_dir(repo_dir)
    file_path = repo_dir / "hello.txt"
    create_file(file_path, "Hello, Dulwich!")
    repo = initialize_repo(repo_dir)
    blob = add_blob_to_repo(repo, file_path)
    tree = create_tree(repo, "hello.txt", blob)
    commit = create_commit(repo, tree, "Alam <alam@example.com>", "Initial commit")
    update_refs_and_index(repo, commit, tree)
    print("Committed to master:", commit.id.decode("ascii"))


if __name__ == "__main__":
    main()
