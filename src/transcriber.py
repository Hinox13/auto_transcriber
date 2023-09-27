import whisper
import torch
import traceback

### CHANGE WHISPER SIZE HERE ###
model_size="medium"
################################

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)

model = whisper.load_model(model_size, device = DEVICE, download_root="./models")

print("transcribing")
def transcribe(path, config={}):
    try:
        if not config:
            config = {
                "task": "transcribe",
            }

        transcription = model.transcribe(path, **config)
        print(transcription)
        print(transcription["text"])
        # Store plain transcript
        f = open("transcripts/transcripts.txt", "w")
        f.write(transcription["text"])
        f.close()
        # Store transcript with date format
        f = open("transcripts/transcripts_in_time.txt", "w")
        transcripts = "\n".join([ f"{segment['start']} - {segment['end']}: {segment['text']}" for segment in transcription["segments"]])
        f.write(transcripts)
        f.close()
    except Exception as e:
        print(e)
        traceback.print_exc()

# Warm up the model
transcribe("audio/Cristiano Ronaldo - Siuuu.mp3")
