from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)

# 아이디 패스워드 추가사항 시작
f = open("idpwd.txt", 'r')
line = f.readline()
a = line.split(',')
ids = a[0]
pwds = a[1]
pwdcerts = a[2]
f.close()

a = "C:\CREON\STARTER\coStarter.exe /prj:cp /id:"
b = " /pwd:"
c = " /pwdcert:"
d = " /autostart"
address = a + ids + b + pwds + c + pwdcerts + d
# 아이디 패스워드 추가사항 끝

app = application.Application()
app.start(address)
time.sleep(60)