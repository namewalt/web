#coding:utf-8

import RPi.GPIO as GPIO
import sys, time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)	#Red
GPIO.setup(38, GPIO.OUT)	#Green
GPIO.setup(40, GPIO.out)	#Blue

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
