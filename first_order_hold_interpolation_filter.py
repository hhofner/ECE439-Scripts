import numpy             as np
import matplotlib.pyplot as plt
from scipy import signal 

Fs  = 100000.0  # Sampling frequency 100,000 Hz 
t_p = 1/Fs      # Time interval

t = np.arange(0.0, 2.0, t_p)  # Time step of 0.0000001 
y = np.sin(300*np.pi*2*t)

# Plot size
plt.figure(figsize=(40,20))

# Plot the input signal
plt.subplot(311)
plt.plot(t, y)
# Zoom into plot
plt.xlim([0,0.05])

# Set every 20,000 value a 1, including last 
pulseTrain = [0 for i in range(len(y))]
for index, val in enumerate(pulseTrain):
    if index % 10 == 0:
        pulseTrain[index] = 1
        pulseTrain[index+1] = 1

pulseTrain[len(pulseTrain)-1] = 1
pulseTrain[len(pulseTrain)-2] = 1 

plt.subplot(312)
plt.plot(t, pulseTrain)
plt.xlim([0,0.23])

sampled = [0 for l in range(len(pulseTrain))]

if len(pulseTrain) != len(y):
    raise Exception("Lengths do not match")

else:
    for indx, val in enumerate(y):
        sampled[indx] = y[indx] * pulseTrain[indx]

plt.subplot(313)
plt.plot(t, sampled)
plt.show()
