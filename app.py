from flask import Flask, request, render_template, redirect, url_for
import threading
import src.transcriber as whisper

import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('transcribe_template.html')

@app.route('/', methods=['POST'])
def transcribe():
    try:
        if "audio_data" in request.files and request.files["audio_data"].filename != '':
            file = request.files["audio_data"]
            file.save(file.filename)
            path=file.filename
        else:
            path = "audio/"+request.form["name"]

        config = {
                "task" : request.form["task"]
            }
        threading.Thread(target=whisper.transcribe, args=(path, config)).start()
        
    except Exception as e:
        print(e)
        traceback.print_exc()
    
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)
