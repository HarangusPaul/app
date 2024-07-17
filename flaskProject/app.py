import subprocess

from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
cors = CORS(app, resources={
    r"/socket.io/*": {
        "origins": ["https://tr-reply-test-ai.ew.r.appspot.com"]
    },
    r"/v1/*": {
        "origins": [
            "https://tr-reply-test-ai.ew.r.appspot.com",
            "http://localhost:3003",
            "http://127.0.0.1"
        ]
    }
})

@app.route('/v1/msg',methods=['POST'])
def command():  # put application's code here
    command = request.get_json()["command"]
    result = subprocess.run(['cmd.exe', '/c', command], capture_output=True, text=True)

    return str(result.stdout)


if __name__ == '__main__':

    app.run()
