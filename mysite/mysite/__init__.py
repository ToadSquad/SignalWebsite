import django
django.setup()
default_app_config = 'myapp.apps.MyAppConfig'

import threading
from .scriptmanager import script
import datetime

print(threading.get_native_id())
runthread = True
try:
    file = open("threadid","r")
    print()
    datetimeStr = file.read()
    print(datetimeStr)
    if(datetime.datetime.strptime(datetimeStr,"%Y-%m-%d %H:%M:%S.%f")>(datetime.datetime.now() - datetime.timedelta(minutes=3))):
        print("Within")
        runthread = False
except:
    print("file error")

file = open("threadid","w")
file.write(str(datetime.datetime.now()))
file.close()
if(runthread):
    instance = script()
    trigger_thread = threading.Thread(target=instance.run, name="triggers")
    trigger_thread.start()
    print("running")