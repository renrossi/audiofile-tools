import numpy as np
import matplotlib.pyplot as plt


# Generates a signal made up of two sinusoids, one at 51 Hz and the other at 247 Hz #

# Width of many of the figures
figWidth = 16

sampleFrequency = 1024

# 0-512 Hz (also Nyquist freq)
bandwidth = sampleFrequency / 2

# time duration per cycle
sampleDuration = 1.0 / sampleFrequency

signalTime = np.arange(0, 1, sampleDuration)
signal1Freq = 51
signal1Samples = np.sin(2.0 * np.pi * signal1Freq * signalTime)
signal2Freq = 247
signal2Samples = np.sin(2.0 * np.pi * signal2Freq * signalTime)
signalSamples = (signal1Samples + signal2Samples) / 2


# Plots the generated signal #

plt.figure(figsize=(figWidth, 4))
plt.plot(signalTime, signalSamples)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.suptitle('Source Signal')
plt.show()
