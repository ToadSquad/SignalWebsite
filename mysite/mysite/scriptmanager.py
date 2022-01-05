from .cryptoOrderBookScanner import BinanceScanner
import datetime
import time
import pickle
class script():
   def __init__(self):
       self.scanner = BinanceScanner(5,2)
       firstRun = True
       while(True):
           if(firstRun or datetime.datetime.now().minute%15==0):
               self.latestTriggers = open("triggers.dat", "wb")
               self.scanner.run()
               data = self.scanner.obTriggerList
               print(data)
               pickle.dump(data, self.latestTriggers)
               self.latestTriggers.close()
               firstRun = False
               print("------------------DONE------------------")
               time.sleep(600)
               

