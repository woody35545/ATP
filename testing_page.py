import calculator as cal
import time as t
import api
from pandas import Series
f = "data.txt"
td = "test_data.txt"
date = [""]
xrp_close = [0.0]
s= Series(xrp_close,date)
cp = api.get_current_price("KRW-XRP")
print(cp)
res= api.get_day_candle("KRW-XRP")
for i in range(5):
    s[res[i]['candle_date_time_kst']] = res[i]['trade_price']
print(s)

#while True:

    #t.sleep(1)