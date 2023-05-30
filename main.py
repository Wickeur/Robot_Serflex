from machine import Pin
import time

def avancer():
    motor1Pin1.low()
    motor1Pin2.high()
    motor2Pin1.low()
    motor2Pin2.high()

def reculer():
    motor1Pin1.high()
    motor1Pin2.low()
    motor2Pin1.high()
    motor2Pin2.low()

def stop():
    motor1Pin1.low()
    motor1Pin2.low()
    motor2Pin1.low()
    motor2Pin2.low()

def pivoterDroite():
    motor1Pin1.high()
    motor1Pin2.low()
    motor2Pin1.low()
    motor2Pin2.high()

def pivoterGauche():
    motor1Pin1.low()
    motor1Pin2.high()
    motor2Pin1.high()
    motor2Pin2.low()

def demitour():
    pivoterDroite()
    sleep(1)

motor1Pin1 = Pin(5, Pin.OUT)
motor1Pin2 = Pin(13, Pin.OUT)
motor2Pin1 = Pin(8, Pin.OUT)
motor2Pin2 = Pin(12, Pin.OUT)
capteurLigne = Pin(18, Pin.IN)
bouton = Pin(20, Pin.IN, Pin.PULL_UP)
peut_avancer = False

while True:

    if bouton.value() == 0:
        peut_avancer = !peut_avancer

    if peut_avancer:
        time.sleep(30)
        if capteurLigne.value() == 1:
            demitour()
        else:
            avancer()


