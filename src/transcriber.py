import whisper
import torch
import traceback
import src.audio_manager as audio_manager
import src.file_manager as file_manager

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

        # Delete files
        file_manager.restart_file("transcripts/transcripts.txt")
        file_manager.restart_file("transcripts/transcripts_in_time.txt")
        # Modify the file to mp3 and 
        audio = audio_manager.x2mp3(path)
        print(f"Must cut audio in {int(audio.duration_seconds//3600)+1} chunks")
        for i in range(int(audio.duration_seconds//3600)+1):
            # Do cut and extract audio
            if i == int(audio.duration_seconds//3600):
                audio_manager.cut_audio(audio, i*3600, int(audio.duration_seconds))
            else: audio_manager.cut_audio(audio, i*3600, (i+1)*3600)
            print(f"Sendind chunk {i} to whisper")
            transcription = model.transcribe("chunk.mp3", **config)
            print(transcription)
            print(transcription["text"])
            # Store plain transcript
            file_manager.extend_file("transcripts/transcripts.txt", transcription["text"])
            # Store transcript with date format
            transcripts = "\n".join([ f"{float(segment['start'])+(i*3600)} - {float(segment['end'])+(i*3600)}: {segment['text']}" for segment in transcription["segments"]]) + "\n"
            file_manager.extend_file("transcripts/transcripts_in_time.txt", transcripts)
    except Exception as e:
        print(e)
        traceback.print_exc()

# Warm up the model, don't remove
transcribe("audio/Cristiano Ronaldo - Siuuu.mp3")
