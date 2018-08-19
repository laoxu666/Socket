# 服务端的流程描述
import socket

server = socket.socket()

ip_port = ("10.0.114.55", 8081)

server.bind(ip_port)

server.listen(5)

print("server waiting.......")

conn, address = server.accept()

print("连接成功")

while True:

    client_data = conn.recv(1024)

    print("客户端对服务端说：" + client_data.decode("utf-8"))

    sendData = input("请输入要回复给客户端的消息：")

    conn.send(sendData.encode("utf-8"))

# 6.服务端关闭
server.close()