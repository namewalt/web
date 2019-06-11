#  *_* coding :  UTF-8 *_*
#  开发人员    :  Walt
#  开发团队    :  www.kkii.club
#  开发时间    :  2019/6/3  17:14
#  文件名称    :  app.py.py
#  开发工具    :  PyCharm

from flask import Flask,render_template
from socket import *
from time import ctime

#1.定义域名和端口号
HOST,PORT = "",6666
#2.创建缓冲区大小
BUFFER_SIZE = 1024
ADDR = (HOST,PORT)
#3.创建服务器的套接字 第一个参数是代表IPv4  第二个参数代表基于TCP的编程协议
tcpServerSocket = socket(AF_INET,SOCK_STREAM)
#4.绑定域名和端口号
tcpServerSocket.bind(ADDR)
#5.坚挺连接
tcpServerSocket.listen(5)
print("****************服务器启动成功,等待客户端连接****************")
#6.定义循环,等待客户端的连
def send_msg(msg):
    # 6.2定义一个循环:开始回复数据

    tcpClientSocket.sendall(msg.encode('utf-8'))  # 给客户端回复消息
    print("回复消息:", msg)
    print("回复时间:", ctime())
    print("============================================================")


    data = tcpClientSocket.recv(BUFFER_SIZE).decode()
    print("接收消息:", data)
while True:
    # 6.1定义一个客户端连接对象(端口号和域名)
    tcpClientSocket, addr = tcpServerSocket.accept()
    print("")
    print("客户端:", addr, "连接中。。。")
    print("")
    print("***********************客户端连接成功***********************")
    print("")
    while True:
        app = Flask(__name__)

        @app.route('/')
        def index():
            return """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <title>天才少年WALT</title>
                    </head>
                    <body>
                    <h1 align="center">WALT</h1>
                    <a align="center" href="/a">up</a>
                    <a align="center" href="/b">down</a>
                    <a align="center"href="/c">left</a>
                    <a align="center" href="/d">right</a>
                    <a align="center" href="/e">stop</a>
                    <a align="center"href="/f">quit</a>
                    </body>
                    </html>
                    """

        @app.route('/a')
        def up():
            print("up")
            msg = "up"
            send_msg(msg)
            return render_template('index.html')

        @app.route('/b')
        def down():
            print("down")
            msg = "down"
            send_msg(msg)
            return render_template('index.html')

        @app.route('/c')
        def left():
            print("left")
            msg = "left"
            send_msg(msg)
            return render_template('index.html')

        @app.route('/d')
        def right():
            print("right")
            msg = "right"
            send_msg(msg)
            return render_template('index.html')

        @app.route('/e')
        def stop():
            print("stop")
            msg = "stop"
            send_msg(msg)
            return render_template('index.html')

        @app.route('/f')
        def quit():
            print("quit")
            msg = "quit"
            send_msg(msg)
            return render_template('index.html')

        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=8080)
            print("****************服务器启动成功,等待客户端连接****************")
    print("***********************客户端断开连接,正在重新等待***********************")
tcpServerSocket.close()
