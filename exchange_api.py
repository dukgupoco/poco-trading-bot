from ib_insync import *

class IBKRClient:
    def __init__(self, host, port, clientId):
        self.ib = IB()
        self.ib.connect(host, port, clientId)

    def get_market_data(self, symbol):
        contract = Forex(symbol)  # 예: EURUSD
        self.ib.qualifyContracts(contract)
        ticker = self.ib.reqMktData(contract)
        self.ib.sleep(2)
        return ticker

# 사용 예시
ibkr = IBKRClient("127.0.0.1", 7497, 1)
data = ibkr.get_market_data("EURUSD")
print(data)
