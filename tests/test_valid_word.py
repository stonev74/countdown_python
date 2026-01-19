import unittest
from unittest.mock import patch, Mock
from src.countdown import valid_word

class TestCountdown(unittest.TestCase):
    def setUp(self):
        self.letters = ['B', 'A', 'C', 'K']

    @patch('src.countdown.requests.get')
    def test_invalid_letter(self, mock_get):
        self.assertEqual(valid_word(self.letters.copy(), 'ape'), False)

    @patch('src.countdown.requests.get')
    def test_valid_letters(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        self.assertEqual(valid_word(self.letters.copy(), 'bac'), True)

    @patch('src.countdown.requests.get')
    def test_real_word(self, mock_get):
        #mocks successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        result = valid_word(self.letters, 'back')
        #check api called with url
        mock_get.assert_called_once_with('https://api.dictionaryapi.dev/api/v1/entries/en/back')
        self.assertTrue(result)

    @patch('src.countdown.requests.get')
    def test_invalid_word(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        result = valid_word(self.letters, 'bac')
        mock_get.assert_called_once_with('https://api.dictionaryapi.dev/api/v1/entries/en/bac')
        self.assertFalse(result)


