from git.util.git_util import (
    create_repo_dir,
    get_repo_dir,
    initialize_repo,
    print_commit_history,
)


def main():
    repo_dir = get_repo_dir("deluwich")
    create_repo_dir(repo_dir)
    repo = initialize_repo(repo_dir)
    print_commit_history(repo)


if __name__ == "__main__":
    main()
