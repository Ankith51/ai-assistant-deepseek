from assistant import AIAssistant

def main():
    api_key = "your_deepseek_api_key"  # Replace with your API key
    assistant = AIAssistant(api_key)
    assistant.start_cli()

if __name__ == "__main__":
    main()
