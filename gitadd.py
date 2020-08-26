## Github Repo Pusher

import os

commit = input("\n  Enter Commit Message: ")

os.system("git add .")
os.system("git commit -m '" + commit + "'")
os.system("git push -u origin master")
print("======== DONE ========")
