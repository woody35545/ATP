import random as r
import time as t

class ticker:
    def __init__(self,_name):
        self.name = _name
        self.hold = False
        self.number_of_hold = 0
        self.current_price = 0
    def update_current_price(self):
        self.current_price = round((self.current_price+r.randrange(-100,101)*0.001),2)
KRW_XRP = ticker("KRW_XRP")

KRW_XRP.current_price = 100

print(KRW_XRP.current_price)
while True:
    KRW_XRP.update_current_price()
    print(KRW_XRP.current_price)
    t.sleep(1)