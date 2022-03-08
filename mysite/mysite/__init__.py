import django
django.setup()
default_app_config = 'myapp.apps.MyAppConfig'

import threading
from .scriptmanager import script
instance = script()
        
trigger_thread = threading.Thread(target=instance.run, name="triggers")
trigger_thread.start()
print("running")