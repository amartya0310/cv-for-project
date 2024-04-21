import cv2
import main
import time
from time import sleep
import RPi.GPIO as GPIO
import threading
import jostick_code as jc

def motor_control():
    # Your motor control code here
    # ...
    m1PUL = 17  # Stepper Drive Pulses
    m1DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
    m3PUL = 20
    m3DIR = 21
    m2PUL = 23
    m2DIR = 22
    m4PUL = 24
    m4DIR = 25

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(m1PUL, GPIO.OUT)
    GPIO.setup(m1DIR, GPIO.OUT)
    GPIO.setup(m3PUL, GPIO.OUT)
    GPIO.setup(m3DIR, GPIO.OUT)
    GPIO.setup(m2PUL, GPIO.OUT)
    GPIO.setup(m2DIR, GPIO.OUT)
    GPIO.setup(m4PUL, GPIO.OUT)
    GPIO.setup(m4DIR, GPIO.OUT)

    duration = 5  # This is the duration of the motor spinning. used for forward direction
    duration_spin = 7500  # duration of the motor spinnig while turning left or right on it current position

    #
    delay = 0.0000001  # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.

    def straight(speed, tright, tleft):
        start_time = time.time()

        def right1(speed, tright, tleft):
            GPIO.output(m1DIR, GPIO.LOW)
            GPIO.output(m3DIR, GPIO.LOW)
            while time.time() - start_time < 0.05:
                GPIO.output(m1PUL, GPIO.HIGH)
                GPIO.output(m3PUL, GPIO.HIGH)

                sleep(speed * tleft)

                GPIO.output(m1PUL, GPIO.LOW)
                GPIO.output(m3PUL, GPIO.LOW)

        def left1(speed, tright, tleft):
            GPIO.output(m2DIR, GPIO.HIGH)
            GPIO.output(m4DIR, GPIO.HIGH)
            while time.time() - start_time < 0.05:
                GPIO.output(m2PUL, GPIO.HIGH)
                GPIO.output(m4PUL, GPIO.HIGH)

                sleep(speed * tright)

                GPIO.output(m2PUL, GPIO.LOW)
                GPIO.output(m4PUL, GPIO.LOW)

        thread1 = threading.Thread(target=left1, args=(speed, tright, tleft,))
        thread2 = threading.Thread(target=right1, args=(speed, tright, tleft,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

    def reverse(speed, tright, tleft):
        start_time = time.time()

        def right1(speed, tright, tleft):
            GPIO.output(m1DIR, GPIO.HIGH)
            GPIO.output(m3DIR, GPIO.HIGH)
            while time.time() - start_time < 0.05:
                GPIO.output(m1PUL, GPIO.HIGH)
                GPIO.output(m3PUL, GPIO.HIGH)

                sleep(speed * tleft)

                GPIO.output(m1PUL, GPIO.LOW)
                GPIO.output(m3PUL, GPIO.LOW)

        def left1(speed, tright, tleft):
            GPIO.output(m2DIR, GPIO.LOW)
            GPIO.output(m4DIR, GPIO.LOW)
            while time.time() - start_time < 0.05:
                GPIO.output(m2PUL, GPIO.HIGH)
                GPIO.output(m4PUL, GPIO.HIGH)

                sleep(speed * tright)

                GPIO.output(m2PUL, GPIO.LOW)
                GPIO.output(m4PUL, GPIO.LOW)

        thread1 = threading.Thread(target=left1, args=(speed, tright, tleft,))
        thread2 = threading.Thread(target=right1, args=(speed, tright, tleft,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

    while True:
        control = jc.getJS()
        ver_left = control['axis2']
        hor_right = control['axis3']
        turning = abs(hor_right)
        tright, tleft = 1, 1
        curve = main.getImageCurve()
        if curve > 0:
            tright, tleft = 1, 100
        if  curve< 0:
            tright, tleft = 100, 1
        speed = 0.0001
        straight(speed, tright, tleft)


    #
    GPIO.cleanup()
    print('Cycling Completed')
    #


#

#


# Create threads for each section
motor_control()

print("Both threads have completed.")