import os
import sys
import sqlite3

connection = [None]
cursor = [None]


def main(args):
    if not istheredb():
        createdb()
        insertdata(args[1])


def istheredb():
    return os.path.isfile('cronhoteldb.db')


def createdb():
    global connection
    connection = sqlite3.connect('cronhoteldb.db')
    with connection:
        global cursor
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE TaskTimes(" +
                       "TaskId integer PRIMARY KEY NOT NULL, " +
                       "DoEvery integer NOT NULL, " +
                       "NumTimes integer NOT NULL)")

        cursor.execute("CREATE TABLE Tasks(" +
                       "TaskId integer NOT NULL REFERENCES TaskTimes(TaskId), " +
                       "TaskName text NOT NULL, " +
                       "Parameter integer)")

        cursor.execute("CREATE TABLE Rooms(" +
                       "RoomNumber integer PRIMARY KEY NOT NULL)")

        cursor.execute("CREATE TABLE Residents(" +
                       "RoomNumber integer NOT NULL REFERENCES Rooms(RoomNumber), " +
                       "FirstName text NOT NULL, " +
                       "LastName text NOT NULL)")


def insertroom(roomnum):
    cursor.execute("INSERT INTO Rooms VALUES(?)", (roomnum,))


def insertresident(roomnum, firstname, lastname):
    cursor.execute("INSERT INTO Residents VALUES(?,?,?)", (roomnum, firstname, lastname,))


def inserttask(taskid, taskname, parameter):
    cursor.execute("INSERT INTO Tasks VALUES(?,?,?)", (taskid, taskname, parameter,))


def inserttasktime(taskid, doevery, numtimes):
    cursor.execute("INSERT INTO TaskTimes VALUES(?,?,?)", (taskid, doevery, numtimes,))


def insertdata(filename):
    inputfilename = filename
    tasksequence = 0

    with open(inputfilename) as inputfile:
        for line in inputfile.read().splitlines():
            lst = line.split(',')
            if lst[0] == "room":
                insertroom(lst[1])
                if len(lst) == 4:
                    insertresident(lst[1], lst[2], lst[3])
            elif lst[0] == "breakfast":
                inserttask(tasksequence, "breakfast", lst[2])
                inserttasktime(tasksequence, lst[1], lst[3])
                tasksequence += 1
            elif lst[0] == "wakeup":
                inserttask(tasksequence, "wakeup", lst[2])
                inserttasktime(tasksequence, lst[1], lst[3])
                tasksequence += 1
            elif lst[0] == "clean":
                inserttask(tasksequence, "clean", 0)
                inserttasktime(tasksequence, lst[1], lst[2])
                tasksequence += 1

    if connection is not None:
        connection.commit()
        connection.close()


if __name__ == '__main__':
    main(sys.argv)
