'''
Code found on 'https://glowingpython.blogspot.com/2011/08/how-to-plot-frequency-spectrum-with.html' 

Written by (presumably) user: JustGlowing
'''

from numpy import sin, linspace, pi
import matplotlib.pyplot as plt
from scipy import fft, arange

def plotSpectrum(y, Fs):
    n   = len(y)
    k   = arange(n)  # array of size n
    T   = n/Fs
    frq = k/T  # two sides of frequency range
    frq = frq[range(n/2)]

    Y = fft(y)/n  # fft compution and normalization
    Y = Y[range(n/2)]

    plt.plot(frq, abs(Y), 'r')  # plotting the spectrum
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|Y(freq)|')

def main():
    Fs = 150.0  # sampling rate
    Ts = 1.0/Fs # sampling interval
    t  = arange(0,1,Ts)  # time vector

    ff = 5;  # frequency of signal
    y  = sin(2*pi*ff*t)

    plt.subplot(2,1,1)
    plt.plot(t,y)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.subplot(2,1,2)
    plotSpectrum(y, Fs)
    plt.show()

if __name__ == "__main__":
    main()
