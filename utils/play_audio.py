import pyaudio
import wave
import sys
from os.path import isfile 

def play(wavfile):
	print('Playing Audio file')

	CHUNK = 1024
	try:
		wf = wave.open(wavfile, 'rb')
	except:
		print('%s is not a .wav file!' % wavfile)
		sys.exit(0)
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
			channels=wf.getnchannels(),
			rate=wf.getframerate(),
			output=True)

	data = wf.readframes(CHUNK)

	while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()

def main():
	wavfile = '../waveforms/yamanote-line.wav'
	if not isfile(wavfile):
		raise Exception('Default \'Yamanote Line\' file does not exist')

	play(wavfile)

if __name__ == "__main__":
	main()
