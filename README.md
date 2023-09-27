# Auto Transcriber
Do you have a video or audio and need the transcription quick? Then you've come to the right place!

This repository contains a small container that runs whisper, a speech to text model. It includes a simple web interface that calls an API powered by Flask. 

---
### Folders

The folders that you should be interested about are:
- transcripts: It contains 'transcripts_in_time.txt' and 'transcripts.txt'.
- audio: Here is where you need to place your audio files if they are longer than 20MB.

---
### Set Up

1. Clone the repository.
2. Do `docker compose up`
3. Go to `0.0.0.0:8000` to access the web interface.

---
### Change the whisper model

By default the project runs on whisper medium size. For this you need about 5GB of VRAM. You can check your computer capacity by doing:

`nvidia-smi`

If your computer doesn't have enough capacity, do the following steps:
1. Check the model that suits you from the table below.
2. Copy the name.
3. Go to src/transcriber.py
4. Change the variable `model_size` with your model name.

Here is a table of the whisper GPU consumption for each model:
|  Size  | Parameters | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |      `large`       |    ~10 GB     |       1x       |


Values extracted from the official [whisper Git repository](https://github.com/openai/whisper/blob/main/README.md).

