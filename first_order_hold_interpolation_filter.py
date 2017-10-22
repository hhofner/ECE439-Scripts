'''
This script samples a simulated continuous signal 
and plays the tone of different signals reconstructed
from different sampling rates, as well 
as plots the reconstructed signals. 

Hans Hofner 
UNM Fall 2017
'''

import numpy             as np
import matplotlib.pyplot as plt
from scipy import signal # use firwin and co.

# Simulated continuous signal.  
Fs  = 100000.0 
t_p = 1/Fs 

t = np.arange(0.0, 2.0, t_p) # 200,000 points 
y = np.sin(300*np.pi*2*t)

plt.subplot(111)
plt.plot(t, y)

# Zoom into plot (looks like a box if from 0 to 2)
plt.xlim([0,0.05])

# Create box train, simulated by consecutive impulses
pulseTrain1 = [0 for i in range(len(y))]
pulseTrain2 = pulseTrain1.copy()
pulseTrain3 = pulseTrain1.copy()
pulseTrain4 = pulseTrain1.copy()

# I'm porting the matlab command:
# pulseTrain(1:10:end) = 1
# pulseTrain(2:10:end) = 1
# etc
[1 if indx % 10 == 0 else val for indx, val in enumerate(pulseTrain1)]
[1 if indx % 10 == 0 else val for indx, val in enumerate(pulseTrain2)]
[1 if indx % 10 == 0 else val for indx, val in enumerate(pulseTrain3)]
[1 if indx % 10 == 0 else val for indx, val in enumerate(pulseTrain4)]

[1 if indx-1 % 10 == 0 else val for indx, val in enumerate(pulseTrain2)]
[1 if indx-1 % 10 == 0 else val for indx, val in enumerate(pulseTrain3)]
[1 if indx-1 % 10 == 0 else val for indx, val in enumerate(pulseTrain4)]

[1 if indx-2 % 10 == 0 else val for indx, val in enumerate(pulseTrain3)]
[1 if indx-2 % 10 == 0 else val for indx, val in enumerate(pulseTrain4)]

[1 if indx-3 % 10 == 0 else val for indx, val in enumerate(pulseTrain3)]
[1 if indx-3 % 10 == 0 else val for indx, val in enumerate(pulseTrain4)]

[1 if indx-4 % 10 == 0 else val for indx, val in enumerate(pulseTrain4)]

# I don't know why I'm doing this
pulseTrain1[len(pulseTrain1)-1] = 1
pulseTrain2[len(pulseTrain1)-1] = 1
pulseTrain3[len(pulseTrain1)-1] = 1
pulseTrain4[len(pulseTrain1)-1] = 1

pulseTrain1[len(pulseTrain1)-2] = 1
pulseTrain2[len(pulseTrain1)-2] = 1
pulseTrain3[len(pulseTrain1)-2] = 1
pulseTrain4[len(pulseTrain1)-2] = 1

pulseTrain2[len(pulseTrain1)-3] = 1
pulseTrain3[len(pulseTrain1)-3] = 1
pulseTrain4[len(pulseTrain1)-3] = 1

pulseTrain3[len(pulseTrain1)-4] = 1
pulseTrain4[len(pulseTrain1)-4] = 1

pulseTrain4[len(pulseTrain1)-5] = 1

sampled1 = [0 for l in range(len(pulseTrain1))]
sampled2 = [0 for l in range(len(pulseTrain2))]
sampled3 = [0 for l in range(len(pulseTrain3))]
sampled4 = [0 for l in range(len(pulseTrain4))]

if len(pulseTrain1) != len(y):
    raise Exception("Lengths do not match")

else:
    for indx, val in enumerate(y):
        sampled1[indx] = y[indx] * pulseTrain1[indx]
		sampled2[indx] = y[indx] * pulseTrain2[indx]
		sampled3[indx] = y[indx] * pulseTrain3[indx]
		sampled4[indx] = y[indx] * pulseTrain4[indx]

# Recover sampling time instances
sampled1Index = [i for (i, val) in enumerate(sampled1) if val > 0] 
sampled2Index = [i for (i, val) in enumerate(sampled2) if val > 0] 
sampled3Index = [i for (i, val) in enumerate(sampled3) if val > 0] 
sampled4Index = [i for (i, val) in enumerate(sampled4) if val > 0] 

sampled1Times = 
sampled2Times = 
sampled3Times =
sampled4Times = 

# Remove non-sampled values
filter(lambda a: a != 0, sampled1)
filter(lambda b: b != 0, sampled2)
filter(lambda c: c != 0, sampled3)
filter(lambda d: d != 0, sampled4)

# Reconstruct the signal using first order hold interpolation filter
numPoles = 150
b = signal.firwin(numPoles, 0.5, window='triang')
s = signal.lfilter(b, 1, sampled)

t2 = np.linspace(0.0, 2.0, len(s)) 

plt.show()

