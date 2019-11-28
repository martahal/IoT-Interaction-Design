import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

print("Rasberry Pi says Hello World")

pixel_pin = board.D18

num_pixels = 1

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

def greenLight():
    pixels.fill((0, 255, 0))
    pixels.show()
    print('Green light')

def yellowLight():
    pixels.fill((255,255,0))
    pixels.show()
    print('Yellow light')

def redLight():
    pixels.fill((255,0,0))
    pixels.show()


