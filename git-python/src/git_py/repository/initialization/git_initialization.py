import os
from pathlib import Path

from git_py.util.git_util import initialize_repository

if __name__ == "__main__":
    repo_path = Path(os.environ["DATA_HOME"]) / "repository" / "my_repo"
    initialize_repository(repo_path)
