from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)

f = open("idpwd.txt", 'r')
line = f.readline()
a = line.split(',')
# print(a[0])
ids = a[0]
pwds = a[1]
pwdcerts = a[2]
# print(ids)
# print(pwds)
# print(pwdcerts)
# print(type(ids))
# print(type(pwds))
# print(type(pwdcerts))
f.close()

a = "C:\CREON\STARTER\coStarter.exe /prj:cp /id:"
b = " /pwd:"
c = " /pwdcert:"
d = " /autostart"
address = a + ids + b + pwds + c + pwdcerts + d
# print(address)
# print(type(address))

app = application.Application()
app.start(address)
time.sleep(60)