from socket import *

s = socket(AF_INET, SOCK_STREAM)
data = ("0.0.0.0", 8000)
s.bind(data)
s.listen(3)
c, addr = s.accept()
print(addr)
item = c.recv(4096)
a = """Http/1.1 200 ok
content-Type:text/html

hello world
"""
print(item.decode())
c.send(a.encode())
s.close()
c.close()