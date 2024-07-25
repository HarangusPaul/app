import json


class Prompt:
    def __init__(self):
        with open('responses.json', 'r') as file:
            data = json.load(file)
        self.r1 = data['r1']
        self.r2 = data['r2']
        self.r3 = data['r3']
        self.q1 = data['q1']
        self.r4 = data['r4']
        self.q2 = data['q2']
        self.r5 = data['r5']
        self.q3 = data['q3']
        self.r6 = data['r6']