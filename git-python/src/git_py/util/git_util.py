import os
from pathlib import Path

import git


def initialize_repository(repo_path: Path):
    print(f"repository path: {repo_path}")
    repo = git.Repo.init(repo_path)
    if not repo.bare:
        print("Repository successfully initialized at {}".format(repo_path))
    else:
        print("Could not initialize repository at {}".format(repo_path))


def create_repo(local_path: Path) -> git.Repo:
    """Initialize a new git repository at the given local path."""
    local_path.mkdir(parents=True, exist_ok=True)
    return git.Repo.init(local_path)


def get_repo(local_path: Path) -> git.Repo:
    """Return a git.Repo object for the given local path."""
    return git.Repo(local_path)


def create_file(file_path: Path, content: str) -> None:
    """Create a file at file_path with the given content."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)


def stage_file(repo: git.Repo, file_path: Path) -> None:
    """Stage the specified file in the repository."""
    repo.index.add([str(file_path)])


def commit_changes(repo: git.Repo, message: str) -> None:
    """Commit staged changes with the given message."""
    repo.index.commit(message)


def push_changes(repo: git.Repo, branch: str) -> None:
    """Push committed changes to the specified remote branch."""
    repo.remote(name="origin").push(branch)


def get_repository_dir(repository_folder: str) -> str:
    """Return the absolute path to the repository folder."""
    repository_path = Path(os.environ["DATA_HOME"]) / "repository"
    return str((repository_path / repository_folder).resolve())


def list_remotes(repo: git.Repo) -> list:
    """Return a list of (name, url) tuples for all remotes."""
    return [(remote.name, remote.url) for remote in repo.remotes]


def create_remote(repo: git.Repo, name: str, url: str):
    """Create a new remote. Return the remote or None if it exists."""
    try:
        return repo.create_remote(name, url=url)
    except git.exc.GitCommandError:
        return None


def get_remote_info(repo: git.Repo, remote_name: str):
    """Return (name, url) for the given remote, or None if not found."""
    for remote in repo.remotes:
        if remote.name == remote_name:
            return (remote.name, remote.url)
    return None


def get_tags(repo):
    """Return the tags of the repository."""
    return repo.tags


def print_tag_info(repo, tag):
    """Print information about a tag."""
    tag_obj = repo.tag(tag)
    print(f"\nTag: {tag}")

    if tag_obj.tag:
        print(f"Tag Message: {tag_obj.tag.message}")
        print(f"Tag Author: {tag_obj.tag.tagger}")
    else:
        print("Lightweight tag (no annotation)")


def print_files_from_git(root, level=0):
    for entry in root:
        print(f"{'-' * 4 * level}| {entry.path}, {entry.type}")
        if entry.type == "tree":
            print_files_from_git(entry, level + 1)


def print_commit_data(commit):
    print("-----")
    print(str(commit.hexsha))
    print(
        '"{}" by {} ({})'.format(
            commit.summary, commit.author.name, commit.author.email
        )
    )
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))
    print("-----")


def print_repository_info(repo):
    print("Repository description: {}".format(repo.description))
    print("Repository active branch is {}".format(repo.active_branch))

    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))

    print("Last commit for repository is {}.".format(str(repo.head.commit.hexsha)))
