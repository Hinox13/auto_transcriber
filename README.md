# Auto Transcriber
Do you have a video or audio and need the transcription quick? Then you've come to the right place!

This repository contains a small container that runs whisper, a speech to text model. It includes a simple web interface that calls an API powered by Flask. 

### Folders

The folders that you should be interested about are:
- transcripts: It contains 'transcripts_in_time.txt' and 'transcripts.txt'.
- audio: Here is where you need to place your audio files if they are longer than 20MB.


### Set Up

1. Clone the repository.
2. Do ```docker compose up```
3. Go to ``0.0.0.0:8000`` to access the web interface

