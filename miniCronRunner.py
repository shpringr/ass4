import os
import time
import hotelWorker
import sqlite3

connection = [None]
cursor = [None]


def istheredb():
    istheredb = os.path.isfile('cronhoteldb.db')
    if istheredb: connecttodb()
    return istheredb


def connecttodb():
    global connection
    connection = sqlite3.connect('cronhoteldb.db')
    with connection:
        global cursor
        cursor = connection.cursor()


def areanytaskleft():
    return gettasksleft()


def decreasenumtimes(taskid):
    cursor.execute("UPDATE TaskTimes SET NumTimes=NumTimes-1 "
                   "WHERE TaskId = ?", (taskid,))
    connection.commit()


def gettasksleft():
    cursor.execute("SELECT t.TaskId, t.TaskName, t.parameter, tt.DoEvery FROM Tasks AS t " +
                   "JOIN TaskTimes AS tt " +
                   "ON t.TaskId = tt.TaskId " +
                   "WHERE tt.NumTimes > 0")
    return cursor.fetchall()


tasktimes = dict()

while istheredb() and areanytaskleft():
    for row in gettasksleft():
        taskid = row[0]
        taskname = row[1]
        parameter = row[2]
        doevery = row[3]
        if tasktimes.get(taskid) is None or doevery + tasktimes[taskid] <= time.time():
            timetook = hotelWorker.dohoteltask(taskname, parameter)
            tasktimes[taskid] = timetook
            decreasenumtimes(taskid)
