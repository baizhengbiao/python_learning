#!/usr/bin/python3
# coding=utf-8

class People:
    name = ""
    age = 0
    __weight = 0 #私有属性

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print('%s说：我年龄是%d岁' % (self.name, self.age))

    def __tell(self):
        print("是同性恋！")

class student(People):
    grade = 1

    def __init__(self, name,age,weight,grade):
        People.__init__(self,name,age,weight)
        self.grade = grade

    def speak(self):
        print("%s说：我年龄是%d,%d年级" % (self.name, self.age, self.grade))
