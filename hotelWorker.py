import time


def getFirstName():
    pass


def getLastName():
    pass


def getemptyrooms():
    return ""
    # rooms should be in ascending order
    pass


def dohoteltask(taskname, parameter):
    timetook = time.time()

    if taskname == "𝑤𝑎𝑘𝑒𝑢𝑝":
        print(getFirstName() + " " + getLastName() +
              "in room" + parameter + " received a wakeup call at " + timetook)
    elif taskname == "breakfast":
        print(getFirstName() + " " + getLastName() +
              "in room" + parameter + " has been served breakfast at " + timetook)
    elif taskname == "clean":
        print("rooms " + getemptyrooms() + " were cleaned at " + timetook)

    return timetook
    pass
