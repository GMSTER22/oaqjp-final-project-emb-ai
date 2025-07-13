import requests
import json

def emotion_detector(text):
    text_to_analyse = text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_dict = { "raw_document": { "text": text_to_analyse } }
    res = requests.post( url, json = input_dict, headers=headers )
    formatted_response = json.loads(res.text)
    
    output = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion_name = '' 
    dominant_emotion_value = 0 

    for emotion in output:
        if output[emotion] > dominant_emotion_value:
            dominant_emotion_name = emotion 
            dominant_emotion_value = output[emotion]
    output['dominant_emotion'] = dominant_emotion_name
    print(output)
