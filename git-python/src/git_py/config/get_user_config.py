from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repo = Repo(Path(__file__).parents[4])

    # To check configuration values, use `config_reader()`
    with repo.config_reader() as git_config:
        print(git_config.get_value("user", "email"))
        print(git_config.get_value("user", "name"))
