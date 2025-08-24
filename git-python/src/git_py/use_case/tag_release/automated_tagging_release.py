from git import Repo


def ci_pipeline(repo_path):
    repo = Repo(repo_path)
    origin = repo.remotes.origin

    # Pull latest changes
    origin.pull()

    # Create a tag for the release
    repo.create_tag("v1.0.0", message="Release v1.0.0")

    # Push the tag
    origin.push(tag="v1.0.0")


if __name__ == "__main__":
    repo_path = "/path/to/repo"
    ci_pipeline(repo_path)
