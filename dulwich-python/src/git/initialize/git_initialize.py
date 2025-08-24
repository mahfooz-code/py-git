from git.util.git_util import create_repo_dir, get_repo_dir, initialize_repo


def main():
    repo_dir = get_repo_dir("deluwich")
    create_repo_dir(repo_dir)
    initialize_repo(repo_dir)


if __name__ == "__main__":
    main()
