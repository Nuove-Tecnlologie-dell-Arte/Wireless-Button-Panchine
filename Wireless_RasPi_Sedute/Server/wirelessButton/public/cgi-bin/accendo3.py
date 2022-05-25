#!/usr/bin/env python3
#f = open("./accendo3", "w")
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.output(22,GPIO.HIGH)
#GPIO.cleanup()
