from ollama import chat


class Brain:

    def __init__(self, model="jarvis"):
        self.model = model
        self.history = []

    def think(self, text):

        self.history.append({
            "role": "user",
            "content": text
        })

        response = chat(
            model=self.model,
            messages=self.history
        )

        answer = response["message"]["content"]

        self.history.append({
            "role": "assistant",
            "content": answer
        })

        return answer
