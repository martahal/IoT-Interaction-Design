from sense_hat import SenseHat
import random
import time

sense = SenseHat()


while True:
    sense.clear((255,20,20))
    time.sleep(3)
    sense.clear((255,40,40))
    time.sleep(3)
    sense.clear(255, 60, 60)
