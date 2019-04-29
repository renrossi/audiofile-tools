import numpy as np
import matplotlib.pyplot as plt

#Command line input functions.
parser = argparse.ArgumentParser(description="Process a PCM .wav file and turn it into a PDM file")
parser.add_argument('-i','--input', help='Inputfile of .wav format', required=True)
parser.add_argument('-o','--output', help='Outputfile in plain text, WARNING: will not check if file exists already', required=False)
args = vars(parser.parse_args())

def pdm(x):
    n = len(x)
    y = np.zeros(n)
    error = np.zeros(n+1)
    for i in range(n):
    	y[i] = 1 if x[i] >= error[i] else 0
        error[i+1] = y[i] - x[i] + error[i]
    return y, error[0:n]

n = 100
fclk = 250e6 # clock frequency (Hz)
t = np.arange(n) / fclk
f_sin = 5e6 # sine frequency (Hz)

x = 0.5 + 0.4 * np.sin(2*np.pi*f_sin*t)
y, error = pdm(x)

plt.plot(1e9*t, x, label='input signal')
plt.step(1e9*t, y, label='pdm signal',  linewidth=2.0)
plt.step(1e9*t, error, label='error')
plt.xlabel('Time (ns)')
plt.ylim(-0.05,1.05)
plt.legend()
plt.show()


plt.figure(figsize=(figWidth, 4))
plt.plot(signalTime, signalSamples)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.suptitle('Source Signal')
plt.show()
