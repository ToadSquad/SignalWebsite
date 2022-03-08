from django.apps import AppConfig
import threading

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'
    #def ready(self):
        
        #from .scriptmanager import script
        #instance = script()
        
        #trigger_thread = threading.Thread(target=instance.run, name="triggers")
        #trigger_thread.start()
        #print("running")
        
        
        