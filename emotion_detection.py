import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions


API_KEY = os.getenv("IBM_API_KEY")
URL = os.getenv("IBM_URL")

authenticator = IAMAuthenticator(API_KEY)

nlu = NaturalLanguageUnderstandingV1(
    version="2022-04-07",
    authenticator=authenticator
)

nlu.set_service_url(URL)


def emotion_detector(text):
    if text is None or text.strip() == "":
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
        "anger": emotions["anger"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "fear": emotions["fear"],
        "disgust": emotions["disgust"],
        "dominant_emotion": dominant_emotion
    }