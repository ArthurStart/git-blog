import os
from sys import argv

try:
    lim1, lim2 = int(argv[1]), int(argv[2])
except:
    try:
        lim1 = int(argv[1])
        lim2 = int(10000)
    except:
        print "PictureBlag needs at least one limit argument"

l = []
for f in os.listdir("images"):
    try:
        n = int(f[4:8])
        if n <= lim2 and n > lim1:
            print "![](/images/IMG_"+str(n)+".JPG)\n"
    except:
        pass
