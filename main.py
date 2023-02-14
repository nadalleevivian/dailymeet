import os
import sys

main = "weixin.exe"
f = os.popen(main)
data = f.readlines()
f.close()

sys.exit(0)