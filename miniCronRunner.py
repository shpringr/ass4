import os
import time
import hotelWorker
import sqlite3

def areanytaskleft():
    return not gettasksleft()
    pass


def decreasenumtimes(taskname):
    pass


def gettasksleft():
    lst=[1,2,4]
    return lst
    pass

def getdoevery(taskname):
    pass

tasktimes= dict()

def istheredb():
    return os.path.isfile('cronhoteldb.db')
    pass

while istheredb() and areanytaskleft():
    for taskname in gettasksleft():
        if getdoevery(taskname) + tasktimes[taskname] >= time.time():
            timetook = hotelWorker.dohoteltask(taskname, "")
            tasktimes[taskname] = timetook
            decreasenumtimes(taskname)