import random as r
import time as t
my_tickers = [""]*10
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


# calculator import 해서 실제 상황과 비슷하게 환경 구성후 테스팅 진행, 이후에 안정화 되면 실제 access_key,secret_key를 가지고 api function을 이용하여 실제로 적용

