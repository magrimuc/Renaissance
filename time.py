import datetime
import os
print(os.getpid())

startpoint = datetime.datetime.now();
while(startpoint  + datetime.timedelta(minutes=1)> datetime.datetime.now()):
    {
        #sleep();
    }
print("fertig")
