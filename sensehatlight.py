from sense_hat import SenseHat
import random
import time

sense = SenseHat()


while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    sense.clear((r,g,b))
    time.sleep(3)

