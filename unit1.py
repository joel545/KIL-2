import sys
import time as t
import random as r 
print ("系統路徑：")
print (sys.path)
print("\n--------------------------------------")
"""
for s in sys.path :
    print(s)

print ("sys.path的資料型態",type(sys.path))
print (t.time,tt)
"""
tt= t.localtime(t.time())
print ("目前時間:%4d年%2d月%2d日"%(tt.tm_year,tt.tm_mon,tt.tm_mday))