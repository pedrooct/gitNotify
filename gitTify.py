# -*- coding: utf-8 -*-

#Imports necessários !
import time
import sys
import os

try:
    import linux.gitTify as linux
except ImportError:
    print "Linux notifications not supported"
    print "Please install punotify"

try:

    import windows10.gitTify as windows10
except ImportError:
    print "windows notifications not supported"
    print "Please install win10toast"


def main(argv):
    if sys.platform.startswith('linux'):
        linux.start(argv)
    elif sys.platform.startswith('win'):
        windows10.start(argv)

    while 1:
        pass

if __name__ == "__main__":
    main(sys.argv)
