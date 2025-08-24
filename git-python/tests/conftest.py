import shutil
from pathlib import Path

import pytest
from git import Repo


@pytest.fixture(name="repo")
def repo_(tmp_path: Path) -> Repo:
    """Create a git repository with fake data and history.

    Args:
        tmp_path: Pytest fixture that creates a temporal Path
    """
    # Copy the content from `tests/assets/test_data`.
    repo_path = tmp_path / "test_data"
    shutil.copytree("tests/assets/test_data", repo_path)

    # Initializes the git repository.
    return Repo.init(repo_path)
