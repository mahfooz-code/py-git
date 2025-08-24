from pathlib import Path

from git import Repo

if __name__ == "__main__":
    repo = Repo(Path(__file__).parents[4])

    with repo.config_writer() as git_config:
        git_config.set_value(
            "user", "email", "mohammadmahfooz.alam@gainwelltechnologies.com"
        )
        git_config.set_value("user", "name", "malamg")
