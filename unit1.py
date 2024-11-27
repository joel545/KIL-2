import sys
import time as t
import random as r
import platform as pf

 
"""
print ("系統路徑：")
print (sys.path)
print("\n--------------------------------------")

for s in sys.path :
    print(s)

print ("sys.path的資料型態",type(sys.path))
print (t.time,tt)


tt= t.localtime(t.time())
print ("目前時間:%4d年%2d月%2d日 %2d:%2d:%2d"%(tt.tm_year,tt.tm_mon,tt.tm_mday,tt.tm_hour,tt.tm_min,tt.tm_sec))

myhour1=myhour2=myhour3=70
print ("myhour1,myhour2,myhour3的值都是：",myhour1)

ct=1
print("起始值：",1)
while ct<= 10:
    print ("NO.",ct,"次",end=' ; ')
    ct  +=1  #ct=ct + 1
print("")    
print("作業系統：", pf.system)
print("版本：", pf.version)
print("python版本：", pf.python_version)


QT = int(input("請輸入你每天的靈修時間(分)："))
print ("你每天靈修",QT,"分鐘",end=":") 
if QT < 10 :
    print ("不錯了！每天與主親近。")
elif QT < 20 :
    print ("哇！你愈來愈有基督的樣式。")
elif QT < 30 :
    print ("讚美主！你是未來「新耶路撒冷城」與主同享榮耀的得勝者。")
"""
YN = input("是否要印出 九九乘法表 (Y/y)：")
if YN =='Y' or YN =='y' :
    print ("九九乘法表如下↓")
else : 
    print ("謝謝，下次再來。")