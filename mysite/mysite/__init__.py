import django
django.setup()
default_app_config = 'myapp.apps.MyAppConfig'

import threading
from .scriptmanager import script

print(threading.get_native_id())
file = open("threadid","a")
file.write(str(threading.get_native_id()))
file.close()
file = open("threadid","r")
print(file.read())

instance = script()
trigger_thread = threading.Thread(target=instance.run, name="triggers")
trigger_thread.start()
print("running")