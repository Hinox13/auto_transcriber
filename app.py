from flask import Flask, request, render_template, redirect, url_for
import threading
import tempfile
import src.transcriber as whisper

import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('transcribe_template.html')

@app.route('/', methods=['POST'])
def transcribe():
    try:
        config = {
                "task" : request.form["task"]
            }
        if "audio_data" in request.files and request.files["audio_data"].filename != '':
            file = request.files["audio_data"]
            with tempfile.NamedTemporaryFile() as f:
                file.save(f.name)
                path=f.name
                whisper.transcribe(path, config)
        else:
            path = "audio/"+request.form["name"]
            threading.Thread(target=whisper.transcribe, args=(path, config)).start()

        
        
        
    except Exception as e:
        print(e)
        traceback.print_exc()
    
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)
