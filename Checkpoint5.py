"""
DAH Checkpoint 5
Alasdair Pedley s1717209
"""

# Imports
from webiopi.devices.sensor.onewiretemp import DS18S20
import time
import matplotlib.pyplot as plt

def main():

    # Create lists for plotting later
    time_list = []
    temp1_list = []
    temp2_list = []
    
    # Record start time so the times recorded are relative to the start
    start_time = time.time()

    # We want to take 50 measurements
    for i in range(50):

        # Define temperature sensors
        tmp1 = DS18S20("10-000803af4d6f")
        tmp2 = DS18S20("10-000803af815e")
        
        # Read temperatures
        temp1 = tmp1.getCelsius()
        temp2 = tmp2.getCelsius()       
        
        # Record time
        current_time = time.time() - start_time

        # Add to lists
        temp1_list.append(temp1)
        temp2_list.append(temp2)
        time_list.append(current_time)
        
    # Plot both temperature vs time plots on the same graph
    plt.plot(time_list, temp1_list)
    plt.plot(time_list, temp2_list)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature vs time for 2 different sensors")
    plt.show()

main()
