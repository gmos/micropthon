# Import the Sensemakers board library and use the display.

from sma8266a import *

i2c, display, led, sensor, board_id = setup_standard()

print('Hallo daar PC')
display.print('Hallo daar oled')
