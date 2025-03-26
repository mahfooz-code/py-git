# Git python client

There are several Python libraries available for interacting with Git repositories. Here are some of the most notable ones:

## 1. GitPython

## 2. Dulwich

1. ✅ Pure Python implementation (no need for Git binary)
2. ✅ Supports low-level Git operations
3. ❌ Limited high-level features

### 📌 Installation of Deluwich

```bash
pip install dulwich
```

### 📌 Example Usage of deluwich

```python
from dulwich.repo import Repo
repo = Repo(".")
print(repo.head())
```

👉 GitHub: https://www.dulwich.io

## 3. Pygit2

1. ✅ Python bindings for libgit2
2. ✅ Fast and efficient
3. ❌ Requires libgit2 (C dependency)

### 📌 Installation of pygit2

```bash
pip install pygit2
```

### 📌 Example Usage of pygit2

```python
Copy
Edit
import pygit2
repo = pygit2.Repository("path/to/repo")
print(repo.head.target)
```

👉 GitHub: https://github.com/libgit2/pygit2

## 4. GitPythonShell (gitpy)

✅ Lightweight wrapper for Git commands
✅ Easy to use
❌ Uses subprocess calls (not as efficient)

### 📌 Installation of gitpy

```bash
pip install gitpy
```

### 📌 Example Usage of gitpy

```python
import gitpy
repo = gitpy.Repo("path/to/repo")
repo.commit("Initial commit")
```

👉 GitHub: https://github.com/leetmike/gitpy

## 5. sh (Git via subprocess)

1. ✅ Directly calls git commands via shell
2. ❌ No native Git API (just executes shell commands)

### 📌 Installation of sh

```bash
pip install sh
```

### 📌 Example Usage of sh

```python
from sh import git
print(git.status())
```

👉 GitHub: https://github.com/amoffat/sh

## Which One to Choose?

| Library      | Pros                          | Cons                        | Best For                    |
| ------------ | ----------------------------- | --------------------------- | --------------------------- |
| GitPython    | High-level API, easy to use   | Requires Git binary         | Scripting, automation       |
| Dulwich      | Pure Python (no dependencies) | Limited high-level commands | Embedded Git operations     |
| Pygit2       | Fast, uses libgit2            | Requires C library          | Performance-sensitive tasks |
| gitpy        | Lightweight, subprocess-based | Less efficient              | Simple Git tasks            |
| sh (Git CLI) | Calls Git directly            | No structured API           | Quick Git commands          |

## 🚀 Recommendation

1. For most cases, use GitPython.
2. For embedded Git operations, try Dulwich.
3. For performance, go with Pygit2.
