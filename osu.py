## OSU Beatmap installer

import os, glob, time

for i in glob.glob("*.osz"):
    print("\nInstalling '" + i + "'...")
    os.startfile(i)
    time.sleep(5)

print("\n===========DONE. You can now delete the folder...")
