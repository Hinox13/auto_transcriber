def restart_file(path):
    f = open(path, "w")
    f.write("")
    f.close()

def extend_file(path, text):
    f = open(path, "a+")
    f.write(text)
    f.close()