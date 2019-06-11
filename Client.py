#  *_* coding :  UTF-8 *_*
#  开发人员    :  Walt
#  开发团队    :  www.kkii.club
#  开发时间    :  2019/6/3  17:56
#  文件名称    :  Client.py
#  开发工具    :  PyCharm

import socket  # 客户端 发送一个数据，再接收一个数据
import sys, time
# coding:utf-8
"""
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)  # Red
GPIO.setup(38, GPIO.OUT)  # Green
GPIO.setup(40, GPIO.out)  # Blue


def red():
    GPIO.output(36, GPIO.HIGH)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)


def green():
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.LOW)


def blue():
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.HIGH)


def black():
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)


def white():
    GPIO.output(36, GPIO.HIGH)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)




"""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
#client.connect(('188.131.150.195', 6666))  # 建立一个链接，连接到本地的6969端口
client.connect(('192.168.188.110', 6666))  # 建立一个链接，连接到本地的6969端口
print("已连接")

while True:
    msg = client.recv(1024).decode()       #接受服务器消息
    print("Receive:",msg)
    data = msg
    """
    if data == 'up':
        red()
    elif data == 'left':
        green()
    elif data == 'right':
        blue()
    elif data == 'down':
        white()
    elif data == 'stop':
        black()

    
    """
    if data == "quit":
        break
    
    data = data.encode()
    client.sendall(data)                   #向服务器发送数据
    data = "ok"
    print("Send:",data)

client.close()
