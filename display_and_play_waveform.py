import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from utils.play_audio import play
import numpy as np
import wave
import sys

wav_file = 'waveforms/yamanote-line.wav'

spf = wave.open(wav_file, 'rb')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
#If Stereo
#if spf.getnchannels() == 2:
#	print('Just mono files')
#	sys.exit(0)
plt.plot(signal)

class ButtonClickProcessor(object):
	def __init__(self, axes, label, wav):
		self._wav = wav
		self.button = Button(axes, label)
		self.button.on_clicked(self.play_wav)

	def play_wav(self, wav):
		play(self._wav)

plt.figure(1)
plt.title('Yamanote Line')
axplay = plt.axes([0.7, 0.05, 0.1, 0.075])
axquit = plt.axes([0.81, 0.05, 0.1, 0.075])

bquit  = Button(axquit, 'Quit')
bply   = ButtonClickProcessor(axplay, 'Play', wav_file)

plt.show()

