import os
import time
from pathlib import Path

from dulwich import porcelain
from dulwich.index import build_index_from_tree
from dulwich.objects import Blob, Commit, Tree, parse_timezone
from dulwich.repo import Repo


def get_repo_dir(repo_dir):
    return Path(os.environ["DATA_HOME"]) / "repo" / repo_dir


def create_repo_dir(repo_dir):
    repo_dir.mkdir(parents=True, exist_ok=True)


def initialize_repo(repo_dir):
    try:
        repo = Repo.init(repo_dir)
        print("Initialized empty Git repository in", repo.path)
        return repo
    except Exception as e:
        print("Error initializing repository:", e)
        repo = Repo(repo_dir)
        return repo


def print_commit_history(repo):
    for entry in repo.get_walker():
        print(f"Commit: {entry.commit.id.decode('ascii')}")
        print(f"Message: {entry.commit.message.decode('utf-8')}")


def create_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)


def add_blob_to_repo(repo, file_path):
    with open(file_path, "rb") as f:
        blob = Blob.from_string(f.read())
        repo.object_store.add_object(blob)
    return blob


def create_tree(repo, filename, blob):
    tree = Tree()
    tree.add(filename.encode(), 0o100644, blob.id)
    repo.object_store.add_object(tree)
    return tree


def create_commit(repo, tree, author, message):
    commit = Commit()
    commit.tree = tree.id
    commit.author = commit.committer = author.encode()
    commit.commit_time = commit.author_time = int(time.time())
    commit.commit_timezone = commit.author_timezone = parse_timezone(b"+0530")[0]
    commit.encoding = b"UTF-8"
    commit.message = message.encode()
    repo.object_store.add_object(commit)
    return commit


def update_refs_and_index(repo, commit, tree):
    repo.refs[b"refs/heads/master"] = commit.id
    build_index_from_tree(repo.path, repo.index_path(), repo.object_store, tree.id)


def clone_repository(repo_url: str, target_dir: Path) -> None:
    """
    Clone a git repository to the target directory.

    Args:
        repo_url (str): The URL of the repository to clone.
        target_dir (Path): The directory where the repo will be cloned.
    """
    try:
        porcelain.clone(repo_url, target_dir)
        print(f"Cloned repository from {repo_url} to {target_dir}.")
    except Exception as e:
        print(f"Error cloning repository: {e}")


def get_repo_config(repo):
    return repo.get_config()


def get_core_filemode(config):
    return config.get("core", "filemode")


def get_remote_url(config, remote_name="origin"):
    return config.get(("remote", remote_name), "url")
