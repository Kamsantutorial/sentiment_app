import unittest
from emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_valid_text(self):
        result = emotion_detector("I love AI")
        self.assertIn("joy", result)

    def test_empty_input(self):
        result = emotion_detector("")
        self.assertEqual(result["status"], 400)


if __name__ == "__main__":
    unittest.main()