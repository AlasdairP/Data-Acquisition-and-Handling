"""
Checkpoint 4
Alasdair Pedley s1717209
"""
import time
# Import GPIO library
import webiopi
from webiopi.devices.digital.pcf8574 import PCF8574A


def main():
    
    # Retrieve GPIO lib
    GPIO = webiopi.GPIO
    
    # Setup chip
    mcp = PCF8574A(0x38)
    
    # Set which PCF8574 GPIO pin is connected to the LED
    #LED0 = 0
    
    # Set pin as output
    #mcp.setFunction(LED0, GPIO.OUT)
    
    # Turn on the LED
    #mcp.digitalWrite(LED0, GPIO.LOW)
    
    """
    Using portWrite.
    portWrite(value) can take any integer value up to 256.
    This corresponds to 2^8 since there are 8 I/Os on the chip and thus 2^8 binary combinations.
    The result of portWrite is a logical progression through the combinations, as follows:
    value             LED#
                0    1    2    3
    1           1    1    1    1
    2           0    1    1    1
    3           1    0    1    1
    4           0    0    1    1
    5           1    1    0    1
    ..
    as you can see, the 1st LED changes every time, the 2nd LED every other time, and the third LED every 4th time.
    So for this experiment with 4 LEDs, the pattern repeats with a periodicity of 16.
    """
        
    for i in range(0,16):
            mcp.portWrite(i)      
            time.sleep(1)
    
    
main()