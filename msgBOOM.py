import requests



def xiaomaizhujiao(phoneNumber):
    a = requests.post('https://api-b.xiaomai5.com/b/send/authcode?p=w',{'phone':phoneNumber})
    print('xiaomaizhujiao:' + a.text)


def youzhengEMS(phoneNumber):
    url = 'http://211.156.201.12:8088/youzheng/ems/security?phone=' + phoneNumber 
    a = requests.get(url)
    print('youzhengEMS:' + a.text)


def youkuLogin(phoneNumber):
    a = requests.post('https://cnpassport.youku.com/newlogin/sms/send.do?appName=youku&fromSite=23',{'phoneCode':'86','loginId':phoneNumber,'countryCode':'CN'})
    print('youkuLogin:' + a.text)




if __name__ == '__main__':
    phoneNumber = input('输入电话号码：')
    xiaomaizhujiao(phoneNumber)
    youzhengEMS(phoneNumber)
    youkuLogin(phoneNumber)