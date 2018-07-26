# -*- coding: utf-8 -*-


#Imports necessários !
import time
import sys
import os

#Se existir um import necessário para o sistema operativo esta variavel passa para 1
redFlag=0

#Verifica se estas bibliotecas estão disponiveis , visto que variam de sistema para sistema
try:
    import linux.gitTify as linux
except ImportError:
    if sys.platform.startswith('linux'):
        print "Linux notifications not supported"
        print "Please install punotify"
        redFlag=1


try:
    import windows10.gitTify as windows10
except ImportError:
    if sys.platform.startswith('win'):
        print "windows notifications not supported"
        print "Please install win10toast"
        redFlag=1


#Verifica o tipo de sistema operativo para executar o serviço!
#Garantindo que assim o sistema de notificações funciona sempre !
def main(argv):
    global redFlag
    if redFlag == 1:
        return
    if sys.platform.startswith('linux'):
        linux.start(argv)
    elif sys.platform.startswith('win'):
        windows10.start(argv)

    while 1:
        time.sleep(60)

if __name__ == "__main__":
    main(sys.argv)
