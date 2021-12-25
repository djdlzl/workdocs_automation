from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

conditions = kiwoom.GetConditionNameList()

condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(codes)