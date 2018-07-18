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


def defineSleep(time):
    if time>300:
        return 1
    elif time/2 > 300:
        return time+5
    return time*2

'''
Esta função vai notificar o utilizador do commit!
'''
def notifyWindows(str,rep):
    toaster.show_toast(rep,str, icon_path=None,duration=5,threaded=True)
    # Wait for threaded notification to finish
    while toaster.notification_active(): time.sleep(0.1)

'''
Esta função vai buscar a ultima entrada de commit, compara a hora , com a ultima hora registada no serviço e com base nisso atualiza e compara com a
hora do ultimo update ! Se necessitar de update notifica o utilizador
'''
def getFeed(rep,branch,idx):
    rep=rep+"/commits/"+branch+".atom"
    timer=1
    while 1:
            try:
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
                        str ="New Commit on "+branch+ " - from: "+name +";\nTitle: "+title+";\nID: "+id+"; \nTime: "+timeUpdate
                        notifyWindows(str,rep)
                        time.sleep(30)
                        time.sleep(timer)
                    else:
                        timer=defineSleep(timer)
                        time.sleep(timer)
                else:
                    timer=defineSleep(timer)
                    time.sleep(timer)
                file.close()
            except:
                print "Erro : Ocorreu um erro feche a aplicação !!"
                return 0

'''
Esta função vai buscar a hora do ultimo update que ocorreu no ramo !
'''
def getLastUpdate(rep):
    file = urllib2.urlopen(rep)
    data = file.read()
    root = ET.fromstring(data)
    lastUpdate= root.find('{http://www.w3.org/2005/Atom}updated').text
    return lastUpdate

'''
Esta função inicia o serviço ,
verifica a rota url e quantos branches tem de seguir e com base nisso abre uma thread para cada um deles !
'''
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
