import os
import sys

f = sys.argv[1]

gif = f.split(".")[-1] + ".gif"
cmd = "ffmpeg -i {} -loop 0 {}".format(f,gif )
print(cmd)
os.system(cmd)