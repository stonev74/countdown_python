import unittest
from src.countdown import award_points


class TestCountdown(unittest.TestCase):
    def test_award_points_nine(self):
        self.assertEqual(award_points('shogunate'), 18)

    def test_award_points_too_long(self):
        self.assertEqual(award_points('helloanyone'), 'Invalid word length!')

    def test_award_points_regular_word(self):
        self.assertEqual(award_points('hello'), 5)

if __name__ == "__main__":
    unittest.main() 