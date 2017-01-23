import time

import sqlite3

connection = [None]
cursor = [None]


def connecttodb():
    global connection
    connection = sqlite3.connect('cronhoteldb.db')
    with connection:
        global cursor
        cursor = connection.cursor()


def getemptyrooms():
    cursor.execute("SELECT r.RoomNumber FROM Rooms r " +
                   "WHERE NOT EXISTS(SELECT 1 FROM Residents rr WHERE r.RoomNumber = rr.RoomNumber) "
                   "ORDER BY r.RoomNumber ASC")
    rooms = ""
    for row in cursor.fetchall():
        rooms += str(row[0]) + ", "
    return rooms[:-2]


def getresident(parameter):
    cursor.execute("SELECT r.FirstName, LastName FROM Residents r " +
                   "WHERE r.RoomNumber = ?", (parameter,))
    return cursor.fetchone()


def dohoteltask(taskname, parameter):
    connecttodb()
    timetook = time.time()

    if taskname == "wakeup":
        row = getresident(parameter)
        print(row[0] + " " + row[1] + " "
                                      "in room " + str(parameter) + " received a wakeup call at " + str(timetook))
    elif taskname == "breakfast":
        row = getresident(parameter)
        print(row[0] + " " + row[1] + " "
                                      "in room " + str(parameter) + " has been served breakfast at " + str(timetook))
    elif taskname == "clean":
        print("rooms " + getemptyrooms() + " were cleaned at " + str(timetook))

    return timetook
