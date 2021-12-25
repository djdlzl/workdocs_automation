from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)


Construction = kiwoom.GetMasterConstruction("005930")
ListedStockData = kiwoom.GetMasterListedStockDate("005930")
LastPrice = kiwoom.GetMasterLastPrice("005930")
StockState = kiwoom.GetMasterStockState("005930")
group = kiwoom.GetThemeGroupList(1)
ticker = kiwoom.GetThemeGroupCode("141")

print(Construction)
print(ListedStockData)
print(LastPrice)
print(StockState)
pprint.pprint(group)
pprint.pprint(ticker)