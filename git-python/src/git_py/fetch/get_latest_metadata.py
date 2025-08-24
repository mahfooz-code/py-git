from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repo = Repo(Path(__file__).parents[4])
    origin = repo.remote("origin")
    assert origin.exists()
    for fetch in origin.fetch():
        print(fetch)
