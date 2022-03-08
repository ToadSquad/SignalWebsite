import dtale
import pandas as pd
import re
import requests
import yfinance
import talib
from talib.abstract import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
#from bokeh.io import output_file, show, vform
import datetime

#To do
#Add Multi Interval Support
#Add More in depth Backtesting for Strategies.
class TAdata():
    def run(self):
        self.symbols = ['EURUSD=X','ETHUSD=X','BTCUSD=X','GBPUSD=X','AUDUSD=X','USDJPY=X','NZDUSD=X','GBPJPY=X','EURGBP=X','EURCAD=X','EURJPY=X','USDCAD=X']
        self.token = 'sk_2ddaab04d2914887bf39d40b7b6d0556'
        #self.getSymbols()
        self.tickerDf = {}
        self.funcs = talib.get_functions()
        self.symboldata = {}
        self.triggerData = {}
        self.refinedTriggers = {}
        print(talib.get_functions())
        self.function_map = {
                'HT_DCPERIOD':HT_DCPERIOD,
        'HT_DCPHASE':HT_DCPHASE,
        'HT_PHASOR':HT_PHASOR,
        'HT_SINE':HT_SINE,
        'HT_TRENDMODE':HT_TRENDMODE,
        'ADD':ADD,
        'DIV':DIV,
        'MAX':MAX,
        'MAXINDEX':MAXINDEX,
        'MIN':MIN,
        'MININDEX':MININDEX,
        'MINMAX':MINMAX,
        'MINMAXINDEX':MINMAXINDEX,
        'MULT':MULT,
        'SUB':SUB,
        'SUM':SUM,
        'ACOS':ACOS,
        'ASIN':ASIN,
        'ATAN':ATAN,
        'CEIL':CEIL,
        'COS':COS,
        'COSH':COSH,
        'EXP':EXP,
        'FLOOR':FLOOR,
        'LN':LN,
        'LOG10':LOG10,
        'SIN':SIN,
        'SINH':SINH,
        'SQRT':SQRT,
        'TAN':TAN,
        'TANH':TANH,
        'ADX':ADX,
        'ADXR':ADXR,
        'APO':APO,
        'AROON':AROON,
        'AROONOSC':AROONOSC,
        'BOP':BOP,
        'CCI':CCI,
        'CMO':CMO,
        'DX':DX,
        'MACD':MACD,
        'MACDEXT':MACDEXT,
        'MACDFIX':MACDFIX,
        'MFI':MFI,
        'MINUS_DI':MINUS_DI,
        'MINUS_DM':MINUS_DM,
        'MOM':MOM,
        'PLUS_DI':PLUS_DI,
        'PLUS_DM':PLUS_DM,
        'PPO':PPO,
        'ROC':ROC,
        'ROCP':ROCP,
        'ROCR':ROCR,
        'ROCR100':ROCR100,
        'RSI':RSI,
        'STOCH':STOCH,
        'STOCHF':STOCHF,
        'STOCHRSI':STOCHRSI,
        'TRIX':TRIX,
        'ULTOSC':ULTOSC,
        'WILLR':WILLR,
        'BBANDS':BBANDS,
        'DEMA':DEMA,
        'EMA':EMA,
        'HT_TRENDLINE':HT_TRENDLINE,
        'KAMA':KAMA,
        'MA':MA,
        'MAMA':MAMA,
        'MAVP':MAVP,
        'MIDPOINT':MIDPOINT,
        'MIDPRICE':MIDPRICE,
        'SAR':SAR,
        'SAREXT':SAREXT,
        'SMA':SMA,
        'T3':T3,
        'TEMA':TEMA,
        'TRIMA':TRIMA,
        'WMA':WMA,
        'CDL2CROWS':CDL2CROWS,
        'CDL3BLACKCROWS':CDL3BLACKCROWS,
        'CDL3INSIDE':CDL3INSIDE,
        'CDL3LINESTRIKE':CDL3LINESTRIKE,
        'CDL3OUTSIDE':CDL3OUTSIDE,
        'CDL3STARSINSOUTH':CDL3STARSINSOUTH,
        'CDL3WHITESOLDIERS':CDL3WHITESOLDIERS,
        'CDLABANDONEDBABY':CDLABANDONEDBABY,
        'CDLADVANCEBLOCK':CDLADVANCEBLOCK,
        'CDLBELTHOLD':CDLBELTHOLD,
        'CDLBREAKAWAY':CDLBREAKAWAY,
        'CDLCLOSINGMARUBOZU':CDLCLOSINGMARUBOZU,
        'CDLCONCEALBABYSWALL':CDLCONCEALBABYSWALL,
        'CDLCOUNTERATTACK':CDLCOUNTERATTACK,
        'CDLDARKCLOUDCOVER':CDLDARKCLOUDCOVER,
        'CDLDOJI':CDLDOJI,
        'CDLDOJISTAR':CDLDOJISTAR,
        'CDLDRAGONFLYDOJI':CDLDRAGONFLYDOJI,
        'CDLENGULFING':CDLENGULFING,
        'CDLEVENINGDOJISTAR':CDLEVENINGDOJISTAR,
        'CDLEVENINGSTAR':CDLEVENINGSTAR,
        'CDLGAPSIDESIDEWHITE':CDLGAPSIDESIDEWHITE,
        'CDLGRAVESTONEDOJI':CDLGRAVESTONEDOJI,
        'CDLHAMMER':CDLHAMMER,
        'CDLHANGINGMAN':CDLHANGINGMAN,
        'CDLHARAMI':CDLHARAMI,
        'CDLHARAMICROSS':CDLHARAMICROSS,
        'CDLHIGHWAVE':CDLHIGHWAVE,
        'CDLHIKKAKE':CDLHIKKAKE,
        'CDLHIKKAKEMOD':CDLHIKKAKEMOD,
        'CDLHOMINGPIGEON':CDLHOMINGPIGEON,
        'CDLIDENTICAL3CROWS':CDLIDENTICAL3CROWS,
        'CDLINNECK':CDLINNECK,
        'CDLINVERTEDHAMMER':CDLINVERTEDHAMMER,
        'CDLKICKING':CDLKICKING,
        'CDLKICKINGBYLENGTH':CDLKICKINGBYLENGTH,
        'CDLLADDERBOTTOM':CDLLADDERBOTTOM,
        'CDLLONGLEGGEDDOJI':CDLLONGLEGGEDDOJI,
        'CDLLONGLINE':CDLLONGLINE,
        'CDLMARUBOZU':CDLMARUBOZU,
        'CDLMATCHINGLOW':CDLMATCHINGLOW,
        'CDLMATHOLD':CDLMATHOLD,
        'CDLMORNINGDOJISTAR':CDLMORNINGDOJISTAR,
        'CDLMORNINGSTAR':CDLMORNINGSTAR,
        'CDLONNECK':CDLONNECK,
        'CDLPIERCING':CDLPIERCING,
        'CDLRICKSHAWMAN':CDLRICKSHAWMAN,
        'CDLRISEFALL3METHODS':CDLRISEFALL3METHODS,
        'CDLSEPARATINGLINES':CDLSEPARATINGLINES,
        'CDLSHOOTINGSTAR':CDLSHOOTINGSTAR,
        'CDLSHORTLINE':CDLSHORTLINE,
        'CDLSPINNINGTOP':CDLSPINNINGTOP,
        'CDLSTALLEDPATTERN':CDLSTALLEDPATTERN,
        'CDLSTICKSANDWICH':CDLSTICKSANDWICH,
        'CDLTAKURI':CDLTAKURI,
        'CDLTASUKIGAP':CDLTASUKIGAP,
        'CDLTHRUSTING':CDLTHRUSTING,
        'CDLTRISTAR':CDLTRISTAR,
        'CDLUNIQUE3RIVER':CDLUNIQUE3RIVER,
        'CDLUPSIDEGAP2CROWS':CDLUPSIDEGAP2CROWS,
        'CDLXSIDEGAP3METHODS':CDLXSIDEGAP3METHODS,
        'AVGPRICE':AVGPRICE,
        'MEDPRICE':MEDPRICE,
        'TYPPRICE':TYPPRICE,
        'WCLPRICE':WCLPRICE,
        'BETA':BETA,
        'CORREL':CORREL,
        'LINEARREG':LINEARREG,
        'LINEARREG_ANGLE':LINEARREG_ANGLE,
        'LINEARREG_INTERCEPT':LINEARREG_INTERCEPT,
        'LINEARREG_SLOPE':LINEARREG_SLOPE,
        'STDDEV':STDDEV,
        'TSF':TSF,
        'VAR':VAR,
        'ATR':ATR,
        'NATR':NATR,
        'TRANGE':TRANGE,
        'AD':AD,
        'ADOSC':ADOSC,
        'OBV':OBV,
        
                }
        self.retrieveTAData()
        self.checkTriggers()
        #self.displaydata()
        #self.backTestPatterns()
    def retrieveTAData(self):
        x=0
        for s in self.symbols:
            indicatordata = {}
            x=x+1
            print(x)
            tickerData = yfinance.Ticker(s)
            try:
                self.tickerDf[s] = tickerData.history(period = "1y")
            except:
                continue
            self.tickerDf[s] = self.tickerDf[s].rename(columns={"Open": "open", "High": "high", "Close": "close","Low" : "low","Volume" : "volume"})
            
            for f in self.funcs:
                if(f.count('CDL')==0):
                    continue
                try:
                    indicatordata[f] = self.function_map[f](self.tickerDf[s])
                except:
                    continue
            self.symboldata[s] = indicatordata
            #if(x==100):
            #    break
    def getSymbols(self):
        url = "https://cloud.iexapis.com/stable/ref-data/iex/symbols?token="+self.token
        r = requests.get(url)
        data = r.text
        tempSymbols = re.findall('"symbol":".\w+',data)
        for s in tempSymbols:
            symbol = s.replace('"symbol":"',"")
            if(len(symbol)<5 and self.symbols.count(symbol)==0):    
                self.symbols.append(symbol)

        print(len(self.symbols))
    def displaydata(self):
        #print(self.triggerData)
        df = pd.DataFrame.from_dict(self.triggerData).T
        d = dtale.show(df, ignore_duplicate=True)
        d.open_browser()
        print(d._url)
        file1 = open('triggers.txt','w')
        file1.write(str(self.triggerData))

    def backTestPatterns(self):
        patternReturns = {}
        for s in self.symboldata:
            print(s)
            for pattern in self.symboldata[s]:
                if(s == self.symbols[0]):
                    patternReturns[pattern] = {}
                    patternReturns[pattern]['POS'] = 0
                    patternReturns[pattern]['NEG'] = 0
                    patternReturns[pattern]['DATA'] = 0
                Postriggers = 0
                Posreturns = 0
                Negstriggers = 0
                Negreturns = 0

                for date, value in self.symboldata[s][pattern].iteritems():
                    try:
                        if(value==0):
                            continue
                        #print(str(date).split(' ')[0])
                        #print(str(datetime.datetime.today()).split(' ')[0])
                        if(str(date).split(' ')[0] == str(datetime.datetime.today()).split(' ')[0]):
                            continue
                        
                        if (value>0):
                            Postriggers = Postriggers + 1
                            tickerData = yfinance.Ticker(s)
                            triggerPrice = self.tickerDf[s].close[str(date)]
                            nextDayPrice = self.tickerDf[s].close[str(date+datetime.timedelta(days=1)).split(' ')[0]]
                            Posreturns += (nextDayPrice/triggerPrice-1)*100
                        if (value<0):
                            Negstriggers = Negstriggers + 1
                            tickerData = yfinance.Ticker(s)
                            triggerPrice = self.tickerDf[s].close[str(date)]
                            nextDayPrice = self.tickerDf[s].close[str(date+datetime.timedelta(days=1)).split(' ')[0]]
                            Negreturns += (nextDayPrice/triggerPrice-1)*100
                    except:
                        continue
                if not (Postriggers==0):
                    patternReturns[pattern]['POS'] += Posreturns/Postriggers
                    patternReturns[pattern]['DATA'] += Postriggers
                if not (Negstriggers==0):
                    patternReturns[pattern]['NEG'] += Negreturns/Negstriggers
                    patternReturns[pattern]['DATA'] += Negstriggers
        for pattern in patternReturns:
            patternReturns[pattern]['POS'] = patternReturns[pattern]['POS']/len(self.symbols)
            patternReturns[pattern]['NEG'] = patternReturns[pattern]['NEG']/len(self.symbols)
        df = pd.DataFrame.from_dict(patternReturns).T
        d = dtale.show(df, ignore_duplicate=True)
        d.open_browser()
        print(patternReturns)
    def checkTriggers(self):
        for s in self.symboldata:
            data = {}
            self.refinedTriggers[s] = []
            for pattern in self.symboldata[s]:
                print(pattern)
                data['date '+pattern] = ''
                data['pattern: '+pattern]= ''
                data['value '+pattern] = ''  
                for index, row in self.symboldata[s][pattern].iteritems():
                    if not (row == 0) and index>=datetime.datetime.today()-datetime.timedelta(days=2):
                        print(s+' Triggered on '+str(row)+' For Pattern '+pattern+' on '+str(index))
                        self.refinedTriggers[s].append(s+' Triggered on '+str(row)+' For Pattern '+pattern+' on '+str(index))
                        data['date '+pattern] = index
                        data['pattern: '+pattern]= pattern
                        data['value '+pattern] = row                                            
                        self.triggerData[s] = data
    def sendToMetatrader(self):
        for s in self.triggerData:
            for pattern in self.symboldata[s]:
                toWrite = ''+s+' '
                if(self.triggerData[s]['value '+pattern]>0):
                    toWrite += 'Buy '
                else:
                    toWrite += 'Sell '
                
TaData = TAdata()