from datetime import datetime,timedelta
import numpy as np
def initialize(context):
        set_universe(universe.DollarVolumeUniverse(floor_percentile=99.5,ceiling_percentile=100.0))
        context.stocks_to_long=5
        context.stocks_to_short=5
        context.rebalance_date=None
        context.rebalance_days=5

# Will be called on every trade event for the securities you specify. 
def handle_data(context, data):
    # Implement your algorithm logic here.
   if context.rebalance_date != None:
     next_date=context.rebalance_date+timedelta(days=context.rebalance_days)
        
   if(context.rebalance_date == None or get_datetime()==next_date):
     context.rebalance_date=get_datetime()
   else:    
     return
        
    import pytz
    est= pytz.timezone("US/Eastern")
    time=est.localize(get_datetime())
    if time.hour == 10 and time.minute == 30:
        for stock in data:
            price= data[stock].open_price
            
    
    if time.hour !=9:
        order(side[24],50) 
    # data[sid(X)] holds the trade event data for that security.
    # context.portfolio holds the current portfolio state.
    
    # Place orders with the order(SID, amount) method.
     
    # TODO: implement your own logic here.
    
     # Using a momentum based trading , simply that if the stock price
            historical_data=history(200,"1d","price)
   fifty_daymean=historical_data.tail(50).mean()
   twohundred_daymean= historical_data.tail()
   diff= fifty_daymean/twohundred_daymean -1
                                    
                                    
    diff=diff.dropna()
    diff.sort()
                                    
    buys= diff[diff>0]
    sells= diff[diff<0]
                                    
    buy_length = min(context.stocks_to_long, len(buys))
    sell_length = min(context.stocks_to_short, len(sells))
    buy_weight= 1.0/buy_length if buy_length !=0 else 0
    sell_weight= 1.0/sell_length if sell_length !=0 else 0
                                    
                                    
    buys.sort()
    sells.sort(ascending=False)
    buys= buys.iloc[:buy_length] if buy_weight !=0 else None
    sells= sells.iloc[:short_length] if sell_weight !=0 else None
    
                                    
    stops= historical_data.iloc[-1] *0.02
                                    
    for sym in data:
           if sells is not None and sym in  sells.index:
                 log.info("Short %s" ,sym.symbol)
                 order_target_percent(sym,short_weight,stop_price=data[sym].price+stops[sym])
           elif buys is not None and sym in  buys.index:
                 log.info("long %s" ,sym.symbol)
                 order_target_percent(sym, buy_weight,stop_price=data[sym].price-stops[sym])
                                    
           else:
                 order_target(sym,0)
                                    
       record(wlong=buy_weight,wshort=sell_weight)
                                    
