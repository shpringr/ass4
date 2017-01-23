from datetime import time


def getFirstName():
    pass


def getLastName():
    pass


def getroomstoclean():
    return ""
    # rooms should be in ascending order
    pass


def dohoteltask(taskname, parameter):
    timebefore = time()

    if taskname == "𝑤𝑎𝑘𝑒𝑢𝑝":
        print(getFirstName() + " " + getLastName() +
              "in room" + parameter + " received a wakeup call at " + timebefore)
    elif taskname == "breakfast":
        print(getFirstName() + " " + getLastName() +
              "in room" + parameter + " has been served breakfast at " + timebefore)
    elif taskname == "clean":
        print("rooms " + getroomstoclean() + " were cleaned at " + timebefore)

    timeafter = time()

    return timeafter - timebefore
    pass
