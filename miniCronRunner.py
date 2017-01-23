import hotelManagement
import hotelWorker

def areanytaskleft():
    pass


while(hotelManagement.istheredb() and areanytaskleft()) :
    taskname = ""
    numtimes = 0
    time = hotelWorker.dohoteltask(taskname, "")
    numtimes -= 1
    print(taskname + " took " + time + " seconds")