from sense_hat import SenseHat
import random

sense = SenseHat()


while True:
    sense.set_pixel(random.randint(0,7),random.randint(0,7), (random.randint(0,255), random.randint(0,255),random.randint(0,255)))
