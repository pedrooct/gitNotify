# -*- coding: utf-8 -*-

from easygui import *
import urllib2
import sys
import os
import subprocess


def prepareArray(arr):
    aux=[]
    countBranch=0
    if arr[0]=="":
        return False
    aux.append(arr[0])
    for x in range(1 , len(arr)):
        if arr[x]!="":
            aux.append(arr[x])
        else:
            countBranch=countBranch+1
    if countBranch==3:
        return False
    return aux

def prepareString(arr):
    noSpace=[]
    for  x in range (0, len(arr)):
        noSpace.append(arr[x].replace(" ",""))
    return noSpace

#Função serve para testar URL do github com os repetivos ramos
def testData(arg):
    for x in range(1, len(arg)):
        rep=arg[0]+"/commits/"+arg[x]+".atom"
        try:
            file = urllib2.urlopen(rep)
            data = file.read()
        except:
            return False
    return True

def prepareCommand(fieldValues):
    dir=os.getcwd()
    str="python " + dir +"/gitTify.py"
    for x in range (0, len(fieldValues)):
        str=str+" "+fieldValues[x]

    return str

def main():
    start=1
    while start!=0:
        msg = "Enter the Github URL and the branches you want to follow "
        title = "gitNotify"
        fieldNames = ["GitHub URL:","Branch:","Branch:","Branch:"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = multenterbox(msg,title, fieldNames)
        fieldValues=prepareArray(fieldValues)
        if fieldValues == False :
            msgbox("OOOPS! something went wrong ! Did you forget something ??", ok_button="OK!")
        else:
            fieldValues=prepareString(fieldValues)
            if testData(fieldValues):
                command=prepareCommand(fieldValues)
                msgbox("Program is now running on the background ! you will see the first pop now !", ok_button="OK!")
                os.popen(command) # Just run the program
            else:
                msgbox("OOOPS! something went wrong ! URl ou branches seems to be wrong !!", ok_button="OK!")


if __name__ == "__main__":
    main()
