from .cryptoOrderBookScanner import BinanceScanner
from .patterndata import TAdata
from .models import triggerData
from .models import patternData
from .cryptoAutoTrader import BinanceTrader
import datetime
import time
import pickle
import requests
class script():
    def run(self):
        self.scanner = BinanceScanner(5,2)
        self.patterndata = TAdata()
        self.trader = BinanceTrader()
        firstRun = True
        while(True):
            if(firstRun or datetime.datetime.now().minute%15==0): 
                self.scanner.run()
                data = self.scanner.obTriggerList
                allTriggers = triggerData.objects.all()
                print(data)
               #check active triggers
                for trigger in triggerData.objects.all().filter(priceEntered="entered"):
                    currentPrice = self.scanner.getPrice(trigger.symbol)
                    if(trigger.direction=="Buy"):
                        trigger.currentPL = str(round((((float(currentPrice)/float(trigger.profit))-1)*100),2))
                    else:
                        trigger.currentPL = str(-1*round((((float(currentPrice)/float(trigger.profit))-1)*100),2))
                        
                    trigger.save()
                    print("--------------RUNNING PRICE CHECK------------------")
                    if(trigger.direction == "Buy"):
                        if(float(trigger.upper)<float(currentPrice)):
                            self.trader.closeTrade(trigger.symbol)
                            trigger.priceEntered = "profit"
                            print("--------------PROFIT------------------")
                        elif(float(trigger.lower)>float(currentPrice)):
                            trigger.priceEntered = "loss"
                            print("--------------LOSS------------------")
                        trigger.save()
                    else:
                       if(float(trigger.upper)<float(currentPrice)):
                           trigger.priceEntered = "loss"
                           print("--------------LOSS------------------")
                       elif(float(trigger.lower)>float(currentPrice)):
                           trigger.priceEntered = "profit"
                           print("--------------PROFIT------------------")
                       trigger.save()
               #Upload to Database
                for trigger in data:
                    
                    if(str(type(data[trigger]))=="<class 'str'>"):
                       triggerArr = data[trigger].split(" ")
                       if(len(triggerData.objects.all().filter(symbol=triggerArr[3]).filter(priceEntered="entered"))==0):
                           #Fear/Greed Index Filter
                           url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"

                           headers = {
                                'x-rapidapi-host': "fear-and-greed-index.p.rapidapi.com",
                                'x-rapidapi-key': "b58bb3460emsh90a32ff9d260c88p1664a2jsnb123a52e7a60"
                                }

                           response = requests.request("GET", url, headers=headers).json()
                           if((response["fgi"]["now"]["value"]>25 and triggerArr[1]=="Buy") or response["fgi"]["now"]["value"]<75 and triggerArr[1]=="Sell"):
                               instance = triggerData(None,triggerArr[3],triggerArr[1],triggerArr[5],triggerArr[7],triggerArr[9],datetime.datetime.now(),"entered","0",triggerArr[11])
                               instance.save()
                               if(triggerArr[1]=="Buy"):
                                   self.trader.openbuyTrade(symbol=triggerArr[3],upper=float(triggerArr[7]),lower=float(triggerArr[9]))
        

                
               #Run Pattern Data
                self.patterndata.run()
                for trigger in self.patterndata.triggerData:
                    for item in self.patterndata.refinedTriggers[trigger]:
                        triggerArr = item.split(" ")
                        instance = patternData(None,triggerArr[0],triggerArr[3],triggerArr[6],datetime.strptime(triggerArr[8]+triggerArr[9],"%Y/%m/%d %H:%M:%S"))
                        instance.save()
               
                firstRun = False
                print("------------------DONE------------------")
                time.sleep(600)
               

