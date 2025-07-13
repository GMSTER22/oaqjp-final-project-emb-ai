import requests

def emotion_detector(text):
    text_to_analyse = text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_dict = { "raw_document": { "text": text_to_analyse } }
    res = requests.post( url, json = input_dict, headers=headers )
    return res.text
