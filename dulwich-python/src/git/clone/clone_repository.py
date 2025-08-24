from git.util.git_util import clone_repository, get_repo_dir


def main():
    repo_url = "https://github.com/dulwich/dulwich.git"
    repo_dir = get_repo_dir("deluwich-clone")
    clone_repository(repo_url, repo_dir)


if __name__ == "__main__":
    main()
