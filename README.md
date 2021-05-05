# ATCSFinalProject

This program takes in a song (either as a local file or as a search from YouTube) and returns a .wav file of the song with bass. The bass track plays the root note of each of the song's chords (detected with SonicAPI.com) as a simple sin wave. Bass will be significantly more audible with headphones.

Necessary modules:

Python:

  pip install numpy

  pip install requests

Bash:

  brew install ffmpeg

  sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
 
  sudo chmod a+rx /usr/local/bin/youtube-dl

Files created:

  final.wav -- .wav file containing original song with bassline

  song.wav -- song as .wav file

  bass.wav -- bassline isolated from song

  chords.txt -- chords of the song as well as what time the chords played at, based on the response from SonicAPI
   
  song.mp3 -- song as .mp3 file if downloaded from YouTube

NOTE: Youtube-dl is only necessary for downloading youtube videos. You do not need to install youtube-dl if you plan to only use local files for this program.
