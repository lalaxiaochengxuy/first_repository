# import time
# def find_zs(n):
#     list01=[]
#     if n >= 0:
#         for r in range(2, n):
#                 if n % r != 0:
#                     list01.append(n)
#
#
#
# def bianli():
#     a = time.time()
#     for i in range(100001):
#         find_zs(i)
# b = time.time()
# print(b - a)


# 求100000以内所有质数之和

import time

def timeit(f):
    def wrapper(*args,**kwargs):
        s_t = time.time()
        res = f(*args,**kwargs)
        e_t = time.time()
        print("函数执行时间：%.6f"%(e_t-s_t))
        return res
    return wrapper

# 判断一个数是不是质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# 求和
@timeit
def prime():
    l = []
    for i in range(1,100001):
        if is_prime(i):
            l.append(i)
    return sum(l)

prime() # 函数执行时间：26.753193









