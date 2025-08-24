from github import Github

# Replace with your GitHub personal access token
g = Github("your_personal_access_token")

user = g.get_user()
print(f"Logged in as: {user.login}")


for repo in user.get_repos():
    print(repo.name)
