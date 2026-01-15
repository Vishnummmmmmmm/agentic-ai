class Memory:
    def __init__(self):
        self.history = []

    def add(self, text: str):
        self.history.append(text)

    def recall(self):
        return self.history[-3:]
