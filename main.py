import os, re, wave, requests, glob, numpy as np
from pathlib import Path

def main():
	bashFile = input('Input the absolute pathname of the song you want to upload (must be less than 50 MB).\nIf you do not have a file to upload, type \'n\': ')
	if bashFile != 'n': f = bashFile.replace('\\', '').strip()
	else:
		bashFile = 'song.mp3'
		f = 'song.mp3'
		search = input("Search for a song on YouTube: ")
		search = search.replace('"', '').replace("'", '')
		os.system("youtube-dl --audio-format \'mp3\' --output \'song.%(ext)s\' -x ytsearch1:\'" + search + "\'")
	print("Retrieving chords...")
	with open(f, 'rb') as song:
		r = requests.post('https://api.sonicapi.com/analyze/chords', data={'access_id': 'b289c0ef-88fd-4886-abc3-f829d7b42ac5'}, files={'input_file': song})
		os.system("ffmpeg -loglevel quiet -y -i " + bashFile + " song.wav")
	if r.ok:
		with open('chords.txt', 'w+') as f: f.write(r.text)
		print("Generating bassline...")
		get_audio(r.text)
		print("The program is done. You can view the final product under final.txt and view remaining files in the directory.")
	else: print("Error in retrieving chords:\n" + r.text)

def get_audio(text):
	with wave.open('song.wav', mode='rb') as song:
		framerate = song.getframerate()
		nframes = song.getnframes()
		sample = song.readframes(nframes)
		channels = song.getnchannels()
	songArray = np.frombuffer(sample, dtype=np.int16).astype(np.float32)
	two_pi_t = 2 * np.pi * np.linspace(0, nframes / framerate, nframes)
	f = {'A': 110, 'A#': 116.54, 'B': 123.47, 'C': 130.81, 'C#': 138.59, 'D': 146.83, 'D#': 155.56, 'E': 82.41, 'F': 87.31, 'F#': 92.5, 'G': 98, 'G#': 103.8, 'N': 0}
	switches = list(map(lambda x: int(float(x) * framerate), re.findall('time=\"(.*?)\"', text)))
	notes = re.findall('(?<=chord=\")[A-Z]#?', text)
	bassArray = 0 * two_pi_t[:switches[0]]
	for i in range(0, len(notes) - 1):
		segment = np.sin(f[notes[i]] * two_pi_t[switches[i]:switches[i+1]])
		bassArray = np.concatenate((bassArray, segment))
	segment = np.sin(f[notes[-1]] * two_pi_t[switches[-1]:])
	bassArray = np.concatenate((bassArray, segment))
	bassArray = np.repeat(bassArray, channels)
	Path('bass.wav').touch(exist_ok=True)
	bassArray = (bassArray * 32767).astype("<h")
	with wave.open('bass.wav', 'wb') as f:
		f.setnchannels(channels)
		f.setsampwidth(2)
		f.setframerate(framerate)
		f.writeframes(bassArray.tobytes())
	audio = ((songArray + bassArray) / 2).astype("<h")
	Path('final.wav').touch(exist_ok=True)
	with wave.open('final.wav', 'wb') as f:
		f.setnchannels(channels)
		f.setsampwidth(2)
		f.setframerate(framerate)
		f.writeframes(audio.tobytes())

if __name__ == '__main__':
	#with open('chords.txt', 'r') as f: get_audio(f.read())
	main()

