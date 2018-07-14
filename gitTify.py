# -*- coding: utf-8 -*-

#Imports necessários !
import thread
import threading
import time
import sys
import re
import pynotify
import json
import urllib2
import xml.etree.ElementTree as ET


def notify(str,rep):
    pynotify.init("gitTify")
    notice = pynotify.Notification(rep, str)
    notice.show()
    time.sleep(5)
    notice.close()
    return

def getFeed(rep,branch):
    rep=rep+"/commits/"+branch+".atom"
    while 1:
            file = urllib2.urlopen(rep)
            data = file.read()
            root = ET.fromstring(data)
            entry=root.find('{http://www.w3.org/2005/Atom}entry')
            id = entry.find('{http://www.w3.org/2005/Atom}id').text
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            timeUpdate = entry.find('{http://www.w3.org/2005/Atom}updated').text
            name = entry.find('{http://www.w3.org/2005/Atom}author')
            name = name.find('{http://www.w3.org/2005/Atom}name').text
            time.sleep(50)
            if timeUpdate != getLastUpdate(rep):
                str ="New Commit on "+branch+ " - from: "+name +";\nTitle:"+title+";\nID:"+id+"; \nTime:"+timeUpdate
                notify(str,rep)
            file.close()


def getLastUpdate(rep):
    file = urllib2.urlopen(rep)
    data = file.read()
    root = ET.fromstring(data)
    lastUpdate= root.find('{http://www.w3.org/2005/Atom}updated').text
    return lastUpdate


def main(argv):
    rep=argv[1];
    sizearg=len(argv)
    try:
        for  x in range(2,sizearg):
             thread.start_new_thread( getFeed, (rep, argv[x]))
    except:
        print "Error: unable to start thread"


    while 1:
        pass

if __name__ == "__main__":
    main(sys.argv)
