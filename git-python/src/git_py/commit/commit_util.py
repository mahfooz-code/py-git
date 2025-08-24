from pathlib import Path

from git import Repo

from git_py.util.git_util import print_commit_data, print_repository_info

COMMITS_TO_PRINT = 5


if __name__ == "__main__":
    # Repo object used to interact with Git repositories
    repo_path = Path(__file__).parents[4]
    repo = Repo(repo_path)

    # check that the repository loaded correctly
    if not repo.bare:
        print("Repo at {} successfully loaded.".format(repo_path))
        print_repository_info(repo)

        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits("master"))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit_data(commit)

    else:
        print("Could not load repository at {} :".format(repo_path))
