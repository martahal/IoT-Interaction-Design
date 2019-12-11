
from sense_hat import SenseHat

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

print("Rasberry Pi says Hello World")




sense = SenseHat()

def greenLight():
    sense.clear((0, 255, 0))
    print('Green light')

def yellowLight():
    sense.clear((255, 255, 0))

    print('Yellow light')

def redLight():
    sense.clear((255, 0, 0))


