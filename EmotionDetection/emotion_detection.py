import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    resp= requests.post(url, json = input_json, headers = header)
    resp_json = json.loads(resp.text)
    output_dict = resp_json['emotionPredictions'][-1]['emotion']
    dominant_emotion = max(output_dict, key= output_dict.get)
    output_dict['dominant_emotion'] =dominant_emotion
    return output_dict
