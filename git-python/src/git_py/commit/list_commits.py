from pathlib import Path

import git

if __name__ == "__main__":
    repo_path = Path(__file__).parents[4]
    repo = git.Repo(repo_path)
    for commit in repo.iter_commits(all=True, max_count=10):
        # paths="README.md"):
        print(commit)
