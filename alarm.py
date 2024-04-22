import datetime
import winsound

def alarm(Timing):
    atime = str(datetime.datetime.now().strptime(Timing, " %I:%M %p") or (Timing, "%I:%M %p"))# or (Timing, "ALARM TO %I:%M %p") or (Timing, "%I:%M %p")) 
    atime = atime[11:-3]
    print(atime)
    Hreal = atime[:2]
    Hreal = int(Hreal)
    Mreal = atime [3:5]
    Mreal = int(Mreal)
    a = (f"Alarm is set for {Timing}")
    print (a)
    while True:
        if Hreal == datetime.datetime.now().hour:
            if Mreal == datetime.datetime.now().minute:
                print ("Alarm is running")
                winsound.PlaySound('abc',winsound.SND_ALIAS)
            elif Mreal<datetime.datetime.now().minute:
                break
if __name__ == '__main__':
    alarm('11:06 AM')