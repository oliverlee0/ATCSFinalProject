# ATCSFinalProject

This program takes in a song (either as a local file or as a search from YouTube) and returns a WAV file of the song with bass. The bass track plays the root note of each of the song's chords (detected with SonicAPI.com) as a simple sin wave. The bass will be significantly more audible with headphones.

Necessary modules:

Python: numpy, requests

  pip install numpy

  pip install requests

Bash: ffmpeg, youtube-dl (YouTube downloader)

  brew install ffmpeg

  sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
 
  sudo chmod a+rx /usr/local/bin/youtube-dl

Files created (files are overwritten each time the program is run):

  final.wav -- WAV file containing original song with bassline

  song.wav -- song as WAV file

  bass.wav -- bassline isolated from song

  chords.txt -- chords of the song as well as what time the chords are played at, based on the response from SonicAPI
   
  song.mp3 -- song as MP3 file if downloaded from YouTube

NOTE: Youtube-dl is only necessary for downloading youtube videos. You do not need to install youtube-dl if you plan to only use local files for this program.
