"""
Checkpoint 3

Alasdair Pedley, s1717209, Tuesday, 3307 (3)

"""

import matplotlib.pyplot as pyplot
import time

def main():
    
    # Import ADC chip libraries
    from webiopi.devices.analog.mcp3x0x import MCP3208

    # Define ADC on Chip Enable 0 (CE0/GPIO8) 
    ADC0 = MCP3208(chip=0)
    
    reading_list = []
    time_list = []
    
    start_time = time.time()
    
    for i in range(80):
    
        # Read ADC channel 0 in Volts. This is the reading from the signal generator.
        reading = ADC0.analogReadVolt(3)
        reading_list.append(reading)
    
        time_list.append(time.time() - start_time)

    time_between_samples = time_list[79]/80
    print(time_between_samples)
    
    sampling_rate = 1/time_between_samples
    print(sampling_rate)
    
    nyquist_freq = sampling_rate/2
    print(nyquist_freq)
    
    
    pyplot.plot(time_list,reading_list)
    pyplot.title("Voltage reading vs time")
    pyplot.xlabel("Elapsed time (s)")
    pyplot.ylabel("Voltage (V)")
    pyplot.show()
    

    
    
    
    
main()