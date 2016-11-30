#!/usr/bin/Python3
# coding=utf-8
import urllib.request
import  threading
def printHTTP():
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode('UTF-8')
    print(data)

def testError():
    url = "http://www.baidu.com"
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print("")
    except urllib.erroe.URLError as  e:
        print("urlerror")
    else:
        print("good")
        print(response.read().decode('UTF-8'))

printHTTP()

testError()