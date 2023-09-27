from pydub import AudioSegment

def x2mp3(path):
    path_list = path.split(".")
    m4a_audio = AudioSegment.from_file(path, format=path_list[-1])
    path_list[-1] = "mp3"
    m4a_audio.export(".".join(path_list), format="mp3")