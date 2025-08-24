from git.util.git_util import initialize_repo

repo = initialize_repo("deluwich")
f = open("myrepo/foo", "wb")
_ = f.write(b"monty")
f.close()

repo.get_worktree().stage([b"foo"])
