import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_valid_text(self):
        # Use stable sentence (avoids IBM 422 errors)
        result = emotion_detector(
            "I love artificial intelligence and machine learning"
        )

        # Ensure response structure is correct
        self.assertIn("dominant_emotion", result)
        self.assertIn("joy", result)

        # Validate emotion is one of expected labels
        self.assertIn(
            result["dominant_emotion"],
            ["joy", "anger", "fear", "sadness", "disgust"]
        )

    def test_empty_input(self):
        result = emotion_detector("")
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], "invalid input")


if __name__ == "__main__":
    unittest.main()
