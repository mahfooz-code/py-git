import os

import pytest
from dulwich.repo import Repo

import git.util.git_util as git_util


@pytest.fixture
def temp_repo_dir(tmp_path):
    # Set up a temporary DATA_HOME for get_repo_dir
    old_data_home = os.environ.get("DATA_HOME")
    os.environ["DATA_HOME"] = str(tmp_path)
    yield tmp_path
    if old_data_home is not None:
        os.environ["DATA_HOME"] = old_data_home
    else:
        del os.environ["DATA_HOME"]


def test_get_repo_dir(temp_repo_dir):
    repo_dir = "myrepo"
    expected = temp_repo_dir / "repo" / repo_dir
    result = git_util.get_repo_dir(repo_dir)
    assert result == expected


def test_create_repo_dir(tmp_path):
    repo_dir = tmp_path / "newrepo"
    assert not repo_dir.exists()
    git_util.create_repo_dir(repo_dir)
    assert repo_dir.exists()
    assert repo_dir.is_dir()


def test_initialize_repo_creates_repo(tmp_path):
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    git_util.initialize_repo(repo_dir)
    assert (repo_dir / ".git").exists() or (repo_dir / "objects").exists()


@pytest.mark.skip(reason="initialize repo")
def test_initialize_repo_existing_repo(tmp_path):
    repo_dir = tmp_path / "repo"
    git_util.initialize_repo(repo_dir)
    # Should not raise if called again
    repo2 = git_util.initialize_repo(repo_dir)
    assert repo2 is not None


def test_create_file(tmp_path):
    file_path = tmp_path / "test.txt"
    content = "hello world"
    git_util.create_file(file_path, content)
    assert file_path.read_text() == content


def test_add_blob_to_repo(tmp_path):
    repo = Repo.init(tmp_path)
    file_path = tmp_path / "file.txt"
    file_path.write_text("blob content")
    blob = git_util.add_blob_to_repo(repo, file_path)
    assert blob.data == b"blob content"
    assert repo.object_store[blob.id].data == b"blob content"


def test_create_tree(tmp_path):
    repo = Repo.init(tmp_path)
    file_path = tmp_path / "file.txt"
    file_path.write_text("tree content")
    blob = git_util.add_blob_to_repo(repo, file_path)
    tree = git_util.create_tree(repo, "file.txt", blob)
    assert b"file.txt" in tree
    assert repo.object_store[tree.id] == tree


def test_create_commit(tmp_path):
    repo = Repo.init(tmp_path)
    file_path = tmp_path / "file.txt"
    file_path.write_text("commit content")
    blob = git_util.add_blob_to_repo(repo, file_path)
    tree = git_util.create_tree(repo, "file.txt", blob)
    commit = git_util.create_commit(repo, tree, "Test Author", "Test commit message")
    assert repo.object_store[commit.id] == commit
    assert commit.message == b"Test commit message"
    assert commit.author == b"Test Author"


def test_update_refs_and_index(tmp_path):
    repo = Repo.init(tmp_path)
    file_path = tmp_path / "file.txt"
    file_path.write_text("index content")
    blob = git_util.add_blob_to_repo(repo, file_path)
    tree = git_util.create_tree(repo, "file.txt", blob)
    commit = git_util.create_commit(repo, tree, "Author", "Msg")
    git_util.update_refs_and_index(repo, commit, tree)
    assert repo.refs[b"refs/heads/master"] == commit.id


@pytest.mark.skip(reason="Output capture issues")
def test_print_commit_history_prints(tmp_path, capsys):
    repo = Repo.init(tmp_path)
    file_path = tmp_path / "file.txt"
    file_path.write_text("history content")
    blob = git_util.add_blob_to_repo(repo, file_path)
    tree = git_util.create_tree(repo, "file.txt", blob)
    commit = git_util.create_commit(repo, tree, "Author", "History message")
    git_util.update_refs_and_index(repo, commit, tree)
    git_util.print_commit_history(repo)
    captured = capsys.readouterr()
    assert "Commit:" in captured.out
    assert "Message:" in captured.out


@pytest.fixture
def mock_clone(monkeypatch):
    class MockClone:
        def __init__(self):
            self.called = False
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.called = True
            self.args = args
            self.kwargs = kwargs

    mock = MockClone()
    monkeypatch.setattr("dulwich.porcelain.clone", mock)
    return mock


def test_clone_repository_success(tmp_path, monkeypatch):
    called = {}

    def fake_clone(repo_url, target_dir):
        called["repo_url"] = repo_url
        called["target_dir"] = target_dir

    monkeypatch.setattr("dulwich.porcelain.clone", fake_clone)
    repo_url = "https://example.com/repo.git"
    target_dir = tmp_path / "cloned"
    git_util.clone_repository(repo_url, target_dir)
    assert called["repo_url"] == repo_url
    assert called["target_dir"] == target_dir


def test_clone_repository_failure(tmp_path, capsys, monkeypatch):
    def fake_clone(repo_url, target_dir):
        raise Exception("fail")

    monkeypatch.setattr("dulwich.porcelain.clone", fake_clone)
    repo_url = "https://example.com/repo.git"
    target_dir = tmp_path / "cloned"
    git_util.clone_repository(repo_url, target_dir)
    captured = capsys.readouterr()
    assert "Error cloning repository" in captured.out
