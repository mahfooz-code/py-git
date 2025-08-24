from dulwich.repo import Repo


def get_repo_config(repo_path="../"):
    repo = Repo(repo_path)
    return repo.get_config()


def get_core_filemode(config):
    return config.get("core", "filemode")


def get_remote_url(config, remote_name="origin"):
    return config.get(("remote", remote_name), "url")


if __name__ == "__main__":
    config = get_repo_config()
    print(get_core_filemode(config))
    print(get_remote_url(config))
