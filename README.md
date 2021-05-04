# ATCSFinalProject

This program takes in a song (either as a local file or as a search from YouTube) and returns a .wav file of the song with bass. The bass track plays the root note of each of the song's chords (detected with an API) as a simple sin wave.

Necessary modules: numpy, requests, ffmpeg, youtube-dl

Python:
pip install numpy
pip install requests

Bash:
brew install ffmpeg
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

NOTE: Youtube-dl is only necessary for downloading youtube videos. You do not need to install youtube-dl if you plan to only use local files for this program.
