from pydub import AudioSegment

def x2mp3(path):
    path_list = path.split(".")
    m4a_audio = AudioSegment.from_file(path, format=path_list[-1])
    path_list[-1] = "mp3"
    m4a_audio.export(".".join(path_list), format="mp3")
    return AudioSegment.from_file(".".join(path_list))

def cut_audio(audio, start_time, end_time):
    # Cut the audio
    cut_audio = audio[start_time*1000:end_time*1000]

    # Save the cut audio to a new file
    cut_audio.export("chunk.mp3", format="mp3")