import subprocess

from flask_cors import CORS
from flask import Flask, request

from prompt import Prompt

app = Flask(__name__)
cors = CORS(app, resources={
    r"/socket.io/*": {
        "origins": ["https://tr-reply-test-ai.ew.r.appspot.com"]
    },
    r"/v1/*": {
        "origins": [
            "https://tr-reply-test-ai.ew.r.appspot.com",
            "http://localhost:3001",
            "http://127.0.0.1"
        ]
    }
})

a = Prompt()
@app.route('/v1/msg',methods=['POST'])
def command():  # put application's code here
    command = request.get_json()["command"]

    if command == a.q2:
        return a.r5

    if command == a.q3:
        return a.r6

    if command == a.q1:
        return a.r4

    if command == "Write me a endpoint in springboot controller":
        return a.r1

    if command == "Write a configuration for cors filter on allow all resources":
        return a.r2

    if command == "Can you write me a basic email sender in spring?":
        return a.r3

    if command == "Give me application of AI Across the SDLC.":
        return "In the project planning and analysis phase, the first stage of the software development lifecycle, the main activities are developing and defining the right approach. It is like preparing for a long journey—you need to know where you are going, what you need, and what can happen. During this step, Artificial Intelligence (AI) is your smart travel advisor that assists you in making good arrangements and coping with any obstacles."
    prompt = "The software development lifecycle (SDLC) is the cost-effective and time-efficient process that development teams use to design and build high-quality software. The goal of SDLC is to minimize project risks through forward planning so that software meets customer expectations during production and beyond."

    if command == "What is sdlc?":
        return prompt

    return a.r4
    command = "dir"
    result = subprocess.run(['cmd.exe', '/c', command], capture_output=True, text=True)
    response = "Here you have the details:\n" + str(result.stdout)




    return response


if __name__ == '__main__':

    app.run()
