"""Emotion detection using the Watson NLP EmotionPredict service."""
import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores with the dominant emotion."""
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    emotion_scores = json.loads(response.text)['emotionPredictions'][0]['emotion']
    emotions = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
    }
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
