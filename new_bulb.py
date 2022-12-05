import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Relay_PIN = 7
GPIO.setup(Relay_PIN, GPIO.OUT)
while(1):
    print ("Bulb is on")
    GPIO.output(Relay_PIN,GPIO.LOW)
    time.sleep(100)
    print("Bulb is off")
    GPIO.output(Relay_PIN,GPIO.HIGH)
    time.sleep(10)
