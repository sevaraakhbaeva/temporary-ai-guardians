from flask import Flask, request, jsonify
from werkzeug import secure_filename
import speech_processor as sp
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

# recordsDir = os.path.join(app.instance_path, "records")

@app.route("/", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        print("POST Request")
        audio = request.files["file"]
        audio.save("./test.wav")
        text = sp.recognize("test.wav")
        os.remove("test.wav")
        return jsonify(text)
        
    text = "Wait for request..."
    return jsonify(text)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = port, debug=False)
