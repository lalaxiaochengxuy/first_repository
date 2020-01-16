from socket import *


# 完成和浏览器的交互
def request(connfd):
    data = connfd.recv(1024)
    item = data.decode().split("\n")[0]
    a = item.split(" ")[1]
    if a == "/":
        b = "Http/1.1 200 ok\r\n"
        b += "content-Type:text/html\r\n"
        b += "\r\n"
        with open("index.html") as f:
            b += f.read()
    else:
        b = "Http/1.1 200 ok\r\n"
        b += "content-Type:text/html\r\n"
        b += "\r\n"
        b += "sorry......."
    connfd.send(b.encode())


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8000))
s.listen(3)
while True:
    connfd, addr = s.accept()
    request(connfd)
