#!/usr/bin/python3
# coding=utf-8

import os
import printwelcome
from  printwelcome import  printwelcomeMul
import myClass
import json
print("----------------第一个程序---------------")
'''
  三个单引号 可以多行注释
  函数的定义与使用
'''
# 单行注释


def area(width, height):
    return width*height


def area(width, height=12):
    return width*height

if __name__ == "__main__":
    # 函数的调用
    print(area(12, 3))
    # 包的导入
    printwelcome.printwelcome()
    printwelcomeMul()
    # 类的引入
    p = myClass.People("knife", 28,180)
    p.speak()

    stu = myClass.student("二狗",23,12,4)
    stu.speak()

    # 当前工作目录，此py所在目录
    print(os.getcwd())

    # Python 字典类型转换为 JSON 对象
    data1 = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }
    # 返回string格式
    json_str = json.dumps(data1)
    print("Python 原始数据：", repr(data1))
    print("JSON 对象：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])
    # 写入到文件
    json.dump(data2, open('setting.json', 'w'))

else:
    print("不能被导入")