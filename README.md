# Data-Acquisition-and-Handling
Autumn 2020 course, consisting of programming a Raspberry Pi. Used the WebIOPi library throughout.

Consisted of 5 Checkpoints, but only 3 included code:

Checkpoint 3: Sampling Analogue Signals

Sinusoidal analogue signal generated by a signal generator.
This is connected to an ADC chip, which is connected to a Raspberry Pi.
The ADC takes a sample roughly every 4ms. From this we can derive the Nyquist frequency.
We then vary the input signal frequency and can identify the maximum frequency that we can still measure correctly (by looking at plots).
It should match the Nyquist frequency. We see a beats pattern at/around the Nyquist frequency.


Checkpoint 4: Input/Output (I/O) expander chips and the I2C BUS

PCF8574AN chip (I2C BUS Expander) connected to the Raspberry Pi.
4 LEDs connected to outputs of the PCF8574AN using negative logic (this is used because the chip is better at sinking current than sourcing it).
Python script written to turn the LEDs on/off in a pattern, using portWrite(<value>)


Checkpoint 5: Temperature Sensors

2 DS182B0 temperature sensors connected to the Raspberry Pi. (Interface is "1 wire")
Can monitor and plot temperature vs time.


