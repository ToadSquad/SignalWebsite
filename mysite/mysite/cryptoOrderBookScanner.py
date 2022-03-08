from binance.client import Client
import time
class BinanceScanner():
    def __init__(self,diff,ratio):
        self.api_key = 'cfDpIoySSCjRBkL4QMN0pXr6V0dp4cUqYMoW91tyKuAiMS5XscZuqKfxpX0sOUG7'
        self.api_secret = 'i5IiWEsnR9gssVXqXDzJS4Us1jAlyWCsH21fuSJ39ITKHTQPDtQdR3fFOH3fwJdI'
        self.client = Client(self.api_key, self.api_secret, {"verify": False, "timeout": 20})
        self.obTriggerList = {}
        self.symbols = ['ETHUSDT','BTCUSDT','XRPUSDT','NEOUSDT','DASHUSDT','LTCUSDT','EOSUSDT','ETCUSDT','DOGEUSDT','LUNAUSDT', 'LINKUSDT', 'ADAUSDT', 'BTTUSDT', 'STORJUSDT', 'DOTUSDT', 'XLMUSDT','SOLUSDT','XMRUSDT','HNTUSDT','ILVUSDT','CAKEUSDT','MATICUSDT','BTTUSDT','IOTAUSDT','OMGUSDT','TRXUSDT','XTZUSDT','ZECUSDT']
        self.diff = diff
        self.ratio = ratio
        #self.symbols = ['BTCUSDT']
        #self.getSymbols()
                
    def getPrice(self,symbol):
        return self.client.get_avg_price(symbol=symbol)['price']           
    def run(self):
        for s in self.symbols:
            self.obTriggerList[s]= {}
            #time.sleep(.2)
            try:
                self.getDepthBook(s)
            except Exception as inst:
                print(s+" failed")
                print(inst)
    def getSymbols(self):
        info = self.client.get_exchange_info()
        sym = info['symbols']
        for x in range(len(sym)):
            if(info['symbols'][x]['symbol'].count("USDT")>0):
                self.symbols.append(info['symbols'][x]['symbol'])
        print("symbols")
        print(self.symbols)

    def getDepthBook(self,symbol):
        
        time.sleep(5)
        depth = self.client.get_order_book(symbol=symbol,limit=5000)
        #print(depth)
        lower = float(depth['bids'][0][0])*(1.00-self.diff/100)
        upper = float(depth['asks'][0][0])*(1.00+self.diff/100)      
        asksTotal = 0
        for x in range(len(depth['asks'])):
                if(float(depth['asks'][x][0])>upper):
                    break
                asksTotal += float(depth['asks'][x][0])*float(depth['asks'][x][1])
        bidsTotal = 0
        for x in range(len(depth['bids'])):
            if(float(depth['bids'][x][0])<lower):
                break
            bidsTotal += float(depth['bids'][x][0])*float(depth['bids'][x][1])
        differential = bidsTotal - asksTotal
        ratio = bidsTotal/asksTotal
        print(differential)
        print(ratio)
        print(depth['bids'][len(depth['bids'])-1][0])
        print(depth['asks'][len(depth['asks'])-1][0])
        if(ratio >= self.ratio):#differential>1000000
            #Secondary Screening Net Inflow aka Motivated Buyers/Sellers

            print('Enter Buy Trade '+symbol+'ratio: '+str(ratio)+'upper: '+format(upper,'.8f') + ' lower: '+format(lower,'.8f'))
            self.obTriggerList[symbol] = 'Enter Buy Trade '+symbol+' ratio: '+str(ratio)+' upper: '+str(upper) + ' lower: '+str(lower)+ ' entered: '+str(depth['bids'][0][0])
            
        elif(ratio <= (1/self.ratio)):#differential<-1000000
            print('Enter Sell Trade'+symbol+'ratio: '+str(ratio)+'upper: '+str(upper) + ' lower: '+str(lower))
            self.obTriggerList[symbol] = 'Enter Sell Trade '+symbol+' ratio: '+str(ratio)+' upper: '+format(upper,'.8f') + ' lower: '+format(lower,'.8f') + ' entered: '+str(depth['bids'][0][0])

