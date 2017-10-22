'''
residue9.m port to Python

Z-transform

given H(z) = (5+2z^-1) / (1-0.8z^-1); causal system

find

1) Impulse response
2) I/O difference equation
3) Determine H(z) and sketch its pole-zero plot.
4) Plot |H(e^jw)| and ^D Phase of H(e^jw).
5) Determine the impulse response h(n)

'''
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from zplane import zplane

zero = np.array([-0.4])
pole = np.array([0.8])
zplane(zero, pole)

# Find N = 100 Point complex frequency response of digital
# filter with b numerator coefficients and a denominator coefficients
# W is the vector in radians/sample between 0 and pi

# Now the 101st element of the array H will correspond to w = pi
# A similar result can be obtained using the third form of the
# freqz function.

N = np.linspace(0.0, 1.0, 100)
W = N*(np.pi / 100)  # these are the frequencies we want

# w : ndarray
#
#  The normalized frequencies at which h was computed, in radians/sample.
#
# h : ndarray
#
#  The frequency response, as complex numbers.
zero = np.array([5, -0.4])
pole = np.array([1, 0.8])
w, h = signal.freqz(zero, pole, W)
magH = abs(h)
phaH = np.angle(h)

plt.subplot(411)
plt.ylabel('Magnitude')
plt.xlabel('frequency in radians per sample')
plt.title('One-Sided Magnitude Response')
plt.plot(w, magH)

plt.subplot(412)
plt.ylabel('Magnitude')
plt.xlabel('frequency in Hz units')
plt.plot((w/(2*np.pi)), magH, 'r')

plt.show()
