from sense_hat import SenseHat
import random
import time

sense = SenseHat()


while True:
    sense.clear((255,0,0))
    time.sleep(3)
    sense.clear((0, 255, 0))
    time.sleep(3)
    sense.clear(255, 255, 0)
