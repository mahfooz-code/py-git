import git

from git_py.util.git_util import (
    create_remote,
    get_repository_dir,
    list_remotes,
    print_remote_info,
)


def main():
    repository_folder = "git-python-lib"
    repository_dir = get_repository_dir(repository_folder)
    repo = git.Repo(repository_dir)

    list_remotes(repo)
    create_remote(repo, "origin2", "git@github.com:mahfooziiitian/git-python-lib2.git")
    print_remote_info(repo, "origin")


if __name__ == "__main__":
    main()
