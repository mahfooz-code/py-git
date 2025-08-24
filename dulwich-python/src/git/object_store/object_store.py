from dulwich.objects import Blob
from dulwich.repo import Repo

repo = Repo.init("myrepo", mkdir=True)


blob = Blob.from_string(b"My file content\n")
print(blob.id.decode("ascii"))
