import os,sys
import time


#
# pid = os.fork()
# if pid < 0:
#     print("创建进程失败")
# elif pid == 0:
#     print("创建新进程")
# else:
#     print("这是老进程")
# print("fork 测试结束")


# def func01():
#     print("求1000000以内整数和")
#     time.sleep(2)
#     print("执行完成")
#
#
# def func02():
#     print("求1000000以内完数和")
#     time.sleep(3)
#     print("执行完成")
#
#
# a = time.time()
# data = os.fork()
# b = 1
# c = 3
#
# if data == 0:
#     func01()
#     b = 2
# else:
#     func02()
#     print("b", b)
# b = time.time()
# print(b - a)

# os._exit(0)
sys.exit()
print("a")

