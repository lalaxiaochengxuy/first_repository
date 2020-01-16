"""
作业：   下面函数要执行10次，4秒之内
"""
import time, os


def func():
    print("你好啊")
    time.sleep(3)
    print("aaaaa")


for i in range(10):
    data = os.fork()
    if data == 0:
        func()
        os._exit(0)
