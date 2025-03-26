# Git python

## Properties

1. ✅ High-level API for Git commands
2. ✅ Object-oriented interface to Git repositories
3. ✅ Good for automation and scripting

## 📌 Installation

```bash
pip install gitpython
```

## 📌 Usage

```python
import git
repo = git.Repo.clone_from("https://github.com/user/repo.git", "local_repo")
print(repo.git.status())
```

## References

1. [👉 GitHub](https://github.com/gitpython-developers/GitPython)
