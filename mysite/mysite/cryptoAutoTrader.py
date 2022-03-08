from binance.client import Client
class BinanceTrader():
    def __init__(self):
        self.api_key = "C39R5yIaqpGXuq8IAIRGEnsAb8WQfGls71anlEziqojmqQlzXnZ1zQVE0grtDCYf"
        self.api_secret = "KZmLckjuyydV4ElDUfUp9ulBU2QugMPFsblDSVqSMkuoAZGSvtqmA4JlpJ2HzOej"
        self.client = Client(self.api_key, self.api_secret, {"verify": True, "timeout": 200},tld='us')
        self.riskPercent = 0.25
    def openbuyTrade(self, symbol, upper, lower):
        try:
            upper = round(upper,4)
            lower = round(lower,4)
            print("BUYING "+symbol)
            info = self.client.get_symbol_info(symbol.replace("USDT","USD"))
            symbol = symbol.replace("USDT","USD")
            balance = self.client.get_asset_balance("USD")['free']
            trade = float(balance)*float(self.riskPercent)
            quantity = round((trade/float(self.client.get_avg_price(symbol=symbol)['price']))/float(info['filters'][2]['stepSize']))*float(info['filters'][2]['stepSize'])
            print(quantity)
            print('self.client.create_order(symbol='+symbol+',side="BUY",type="MARKET",quantity='+str(quantity)+')')
            self.client.create_order(symbol=symbol,side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=quantity)
            filledBalance = (self.client.get_asset_balance(symbol.replace("USDT",""))['free']/float(info['filters'][2]['stepSize']))*float(info['filters'][2]['stepSize'])
            print('self.client.create_order(symbol='+symbol+',side="SELL",type="STOP_LOSS_LIMIT",quantity='+str(quantity)+',stopPrice='+str(lower)+')')
            self.client.create_order(symbol=symbol,timeInForce="GTC" ,side=Client.SIDE_SELL,type=Client.ORDER_TYPE_STOP_LOSS,quantity=filledBalance,stopPrice=lower,price=round(lower*.75,2))
            #print('self.client.create_order(symbol='+symbol+',side="SELL",type="TAKE_PROFIT_LIMIT",quantity='+str(quantity)+',stopPrice='+str(upper)+')')
            #self.client.create_order(symbol=symbol,timeInForce="GTC",side=Client.SIDE_SELL,type=Client.ORDER_TYPE_TAKE_PROFIT,quantity=filledBalance,stopPrice=upper,price=round(upper*1.25,2))
        except:
            print("no balance or bad symbol: "+symbol)
    def closeTrade(self,symbol):
        try:
            info = self.client.get_symbol_info(symbol.replace("USDT","USD"))
            filledBalance = (self.client.get_asset_balance(symbol.replace("USDT",""))['free']/float(info['filters'][2]['stepSize']))*float(info['filters'][2]['stepSize'])
            self.client.cancel_order(symbol)
            self.client.create_order(symbol=symbol,side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=filledBalance)
        except:
            print(symbol+" Failed to close, possibly not traded")
    