# 客户端的流程描述
# 导入模块，socket中内置了数据交互的功能
import socket

# 1.创建一个socket的对象
skt = socket.socket()

ip_port = ("10.0.114.55", 8081)

skt.connect(ip_port)

while True:

    sendData = input("请输入发送给服务端的信息：")

    skt.send(sendData.encode("utf-8"))

    # 接收从服务端返回来的信息
    info = skt.recv(1024)
    print("从服务端回复过来的消息:" + info.decode("utf-8"))

# 4.客户端关闭
skt.close()
