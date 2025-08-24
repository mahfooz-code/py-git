from time import time

from dulwich.objects import Blob, Commit, Tree, parse_timezone


def create_blob(content="empty"):
    return Blob.from_string(content)


def create_tree(tag, permissions, blob_id):
    tree = Tree()
    tree.add(tag, permissions, blob_id)
    return tree


def create_commit(tree_id, author, message, tz_offset="-0200", encoding="UTF-8"):
    commit = Commit()
    commit.tree = tree_id
    commit.author = commit.committer = author
    now = int(time())
    commit.commit_time = commit.author_time = now
    tz = parse_timezone(tz_offset)[0]
    commit.commit_timezone = commit.author_timezone = tz
    commit.encoding = encoding
    commit.message = message
    return commit


def tag_repo(
    tag, author, message, content="empty", permissions=0o100644, tz_offset="-0200"
):
    blob = create_blob(content)
    tree = create_tree(tag, permissions, blob.id)
    commit_message = "Tagging repo: " + message
    commit = create_commit(tree.id, author, commit_message, tz_offset)
    return blob, tree, commit


# Example usage:
# blob, tree, commit = tag_repo("v1.0", "John Smith", "Initial tag")
