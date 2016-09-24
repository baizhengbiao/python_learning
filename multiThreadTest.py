#!usr/bin/python3
#coding=utf-8
import _thread
import  threading
import time

'''
    _thread 线程的使用方法

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

if __name__ == "__main__":
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 1,))
        _thread.start_new_thread(print_time, ("Thread-2", 1,))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass
'''

'''
    threading 线程的使用方法
'''
ThreadExitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.name = name
        self.counter = counter


    def run(self):
        print("开始线程："+ self.name)
        print_time(self.name,self.counter,5)
        print("结束线程："+ self.name)


def print_time(threadName,delay,counter):
    while counter:
        if ThreadExitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")