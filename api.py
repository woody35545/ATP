import requests
def get_day_candle(_ticker):
    url = "https://api.upbit.com/v1/candles/days"
    querystring = {"market": _ticker, "count": "5"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    return res

def get_current_price(_ticker):
    res = get_day_candle(_ticker)[0]['trade_price']
    return res

