import json  # Standard library import
import requests  # Third-party import

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the provided text using an external service.

    Args:
        text_to_analyze (str): The text for which emotion is to be analyzed.

    Returns:
        dict: A dictionary containing the emotion label and score, or None if the request fails.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        formatted_response = response.json()  # Use json() directly
        # Accessing the emotion predictions
        emotion_predictions = formatted_response.get('emotionPredictions', [])
        
        if emotion_predictions:
            # Assuming we only care about the first prediction
            emotions = emotion_predictions[0].get('emotion', {})
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Finding the dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Creating the output dictionary
            output = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            output = None
    else:
        output = {'error': 'Request failed with status code ' + str(response.status_code)}

    return output
