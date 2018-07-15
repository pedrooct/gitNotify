# -*- coding: utf-8 -*-

#Imports necessários !
import thread
import threading
import time
import sys
import pynotify
import urllib2
import xml.etree.ElementTree as ET
from win10toast import ToastNotifier #pip install win10toast


#Array Global de controlo de Hora de update para cada thread
lastReadUpdate = []


def notifyWindows(str,rep):
    toaster.show_toast(rep,str, icon_path=None,duration=5,threaded=True)
    # Wait for threaded notification to finish
    while toaster.notification_active(): time.sleep(0.1)


def getFeed(rep,branch,idx):
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
            global lastReadUpdate
            if lastReadUpdate[idx]!=timeUpdate:
                lastReadUpdate[idx]=timeUpdate
                if timeUpdate == getLastUpdate(rep):
                    str ="New Commit on "+branch+ " - from: "+name +";\nTitle:"+title+";\nID:"+id+"; \nTime:"+timeUpdate
                    notifyWindows(str,rep)
                    time.sleep(200)
                else:
                    time.sleep(50)
            else:
                time.sleep(100)
            file.close()



def getLastUpdate(rep):
    file = urllib2.urlopen(rep)
    data = file.read()
    root = ET.fromstring(data)
    lastUpdate= root.find('{http://www.w3.org/2005/Atom}updated').text
    return lastUpdate


def start(argv):
    rep=argv[1]
    sizearg=len(argv)
    global lastReadUpdate
    lastReadUpdate.append("")
    lastReadUpdate.append("")
    try:
        for  x in range(2,sizearg):
            lastReadUpdate.append("")
            thread.start_new_thread( getFeed, (rep,argv[x],x))

    except:
        print "Error: unable to start thread"
