import numpy             as np
import matplotlib.pyplot as plt
from scipy import signal # use firwin and co.

Fs  = 100000.0 
t_p = 1/Fs 

t = np.arange(0.0, 2.0, t_p)  # Time step of 0.0000001 
y = np.sin(300*np.pi*2*t)

# Plot the input signal
plt.subplot(311)
plt.title('Input Signal; 100kHz')
plt.plot(t, y)
# Zoom into plot
plt.xlim([0,0.05])

# Set every 20,000 value a 1, including last 
pulseTrain = [0 for i in range(len(y))]
for index, val in enumerate(pulseTrain):
    if index % 10 == 0:
        pulseTrain[index] = 1
        pulseTrain[index+1] = 1
        pulseTrain[index+2] = 1
        pulseTrain[index+3] = 1
        pulseTrain[index+4] = 1

pulseTrain[len(pulseTrain)-1] = 1
pulseTrain[len(pulseTrain)-2] = 1 

plt.subplot(312)
plt.title('Impulse Box Train')
plt.plot(t, pulseTrain)
plt.xlim([0,0.005])

sampled = [0 for l in range(len(pulseTrain))]

if len(pulseTrain) != len(y):
    raise Exception("Lengths do not match")

else:
    for indx, val in enumerate(y):
        sampled[indx] = y[indx] * pulseTrain[indx]

# Remove non-sampled values
filter(lambda a: a != 0, sampled)

# Reconstruct the signal using first order hold interpolation filter
numPoles = 150
b = signal.firwin(numPoles, 0.5, window='triang')
s = signal.lfilter(b, 1, sampled)

t2 = np.linspace(0.0, 2.0, len(s)) 
#t2 = np.arange(0.0, 2.0, (1/(len(s)+1)))

plt.subplot(313)
plt.title('Sampled')
plt.plot(t, sampled)
plt.plot(t2, s, color='red')
plt.xlim([0,0.05])
plt.show()

