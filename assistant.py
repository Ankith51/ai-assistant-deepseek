from api_client import DeepSeekClient

class AIAssistant:
    def __init__(self, api_key):
        self.client = DeepSeekClient(api_key)

    def respond(self, user_input):
        response = self.client.send_message(user_input)
        return response

    def start_cli(self):
        print("Welcome to the AI Assistant! Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            response = self.respond(user_input)
            print(f"Assistant: {response}")
