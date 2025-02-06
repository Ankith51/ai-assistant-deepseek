import unittest
from assistant import AIAssistant
from unittest.mock import patch

class TestAIAssistant(unittest.TestCase):
    @patch('api_client.DeepSeekClient.send_message')
    def test_respond(self, mock_send_message):
        mock_send_message.return_value = "Hello, how can I help you?"
        assistant = AIAssistant("fake_api_key")
        response = assistant.respond("Hi")
        self.assertEqual(response, "Hello, how can I help you?")
