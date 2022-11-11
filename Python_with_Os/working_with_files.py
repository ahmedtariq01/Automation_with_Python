import os
os.remove("tst.txt")
os.rename("tst.txt","tst2.txt")
os.path.exists("tst.txt")
os.path.getsize("tst.txt")
os.path.getmtime("tst.txt")

import datetime
timestamp = os.path.getmtime("tst.txt")
datetime.datetime.fromtimestamp(timestamp)

os.path.abspath("tst.txt")
os.path.getmtime("tst.txt")
print(os.getcwd())
os.mkdir("new_dir")
os.chdir("new_dir")
os.getmtime("tst.txt")
os.rmdir("new_dir")
os.listdir("new_dir")
os.path.join("new_dir","tst.txt")