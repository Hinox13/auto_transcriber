import whisper
from faster_whisper import WhisperModel
import torch
import traceback
import src.audio_manager as audio_manager
import src.file_manager as file_manager

### CHANGE WHISPER SIZE HERE ###
model_size="large-v2"
################################

SAMPLE_RATE = 16000
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)

# model = whisper.load_model(model_size, device = DEVICE, download_root="./models")
# Run on GPU with FP16
model = WhisperModel(model_size, device=DEVICE,  download_root="./models", compute_type="float16")

print("transcribing")
def transcribe(path, config={}):
    try:
        if not config:
            config = {
                "task": "transcribe",
            }
        # Delete files
        file_manager.restart_file("transcripts/transcripts.txt")
        file_manager.restart_file("transcripts/transcripts_in_time.txt")
        # Get numpy array of the data
        # audio = audio_manager.x2mp3(path)
        file_data = whisper.load_audio(path)
        transcription = ""
        print(f"Must cut audio in {int(len(file_data)//(SAMPLE_RATE*3600))+1} chunks")
        for i in range(int(len(file_data)//(SAMPLE_RATE*3600))+1):
            # Do cut
            if i == int(len(file_data)//(SAMPLE_RATE*3600)):
                chunk = file_data[i*(SAMPLE_RATE*3600): int(len(file_data))]
            else: chunk = file_data[i*(SAMPLE_RATE*3600): (i+1)*(SAMPLE_RATE*3600)]
            print(f"Sendind chunk {i} to whisper")
            segments, info = model.transcribe(chunk, **config)
            # Store plain transcript
            transcript = " ".join([segment.text for segment in segments])
            print(transcript)
            file_manager.extend_file("transcripts/transcripts.txt", transcript)
            # Store transcript with date format
            transcripts = "\n".join([ f"{float(segment.start)+(i*3600)} - {float(segment.end)+(i*3600)}: {segment.text}" for segment in segments if segment.no_speech_prob<0.8]) + "\n"
            file_manager.extend_file("transcripts/transcripts_in_time.txt", transcripts)
    except Exception as e:
        print(e)
        traceback.print_exc()

# Warm up the model, don't remove
print("Warming up the model")
transcribe("audio/Cristiano Ronaldo - Siuuu.mp3")
