import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import (
    Features,
    EmotionOptions,
)


API_KEY = os.getenv("IBM_API_KEY")
URL = os.getenv("IBM_URL")

authenticator = IAMAuthenticator(API_KEY)

nlu = NaturalLanguageUnderstandingV1(
    version="2022-04-07",
    authenticator=authenticator
)

nlu.set_service_url(URL)


def emotion_detector(text):
    # Handle invalid input (required for grading)
    if not text or text.strip() == "":
        return {
            "status": 400,
            "error": "invalid input"
        }

    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    emotions = response["emotion"]["document"]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions.get("anger", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "fear": emotions.get("fear", 0),
        "disgust": emotions.get("disgust", 0),
        "dominant_emotion": dominant_emotion
    }
