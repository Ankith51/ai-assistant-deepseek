import requests

class DeepSeekClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def send_message(self, prompt):
        data = {
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.7
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("text", "No response generated.").strip()
        return f"Error: {response.status_code} - {response.text}"
