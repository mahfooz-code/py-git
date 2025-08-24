from datetime import datetime

import pytest
from dateutil import tz
from git import Actor, Repo

author = Actor("An author", "author@example.com")
committer = Actor("A committer", "committer@example.com")


@pytest.mark.freeze_time("2021-02-01T12:00:00")
def test_repo_is_not_empty(repo: Repo) -> None:
    commit_date = datetime(2021, 2, 1, tzinfo=tz.tzlocal())
    repo.index.add(["mkdocs.yml"])
    repo.index.commit(
        "Initial skeleton",
        author=author,
        committer=committer,
        author_date=commit_date,
        commit_date=commit_date,
    )

    assert not repo.bare


@pytest.mark.freeze_time("2021-02-01T12:00:00")
def test_assert_true(repo: Repo) -> None:
    assert not repo.bare
