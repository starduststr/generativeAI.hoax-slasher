from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request
import requests as reqs
from datetime import datetime

class PredictionScrappingResource(Resource):
    @classmethod
    def upToApi(cls,id, data):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%Y")
        
        method = "PATCH"
        url = f"https://mfsz3q3f-4100.asse.devtunnels.ms/news/predict/{id}"
        params = {
            'label': data['label'],
            'is_ambiguous': data['is_ambiguous'],
            'is_training': 'true',
            'training_date': f'{formatted_date}',
            'news_emotion': data['news_emotion']
            }
        response = reqs.request(method, url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            # print(data)
        else:
            print(response.status_code)
        return response.status_code
            
    @classmethod
    def parsing(cls, data):
        data_list = data.split(" - ")

        hoax = data_list[0].split(":")[1]
        ambigous = data_list[1].split(":")[1]
        emotion = data_list[2].split(":")[1]
        
        # print(hoax, ambigous, emotion)
        return hoax, ambigous, emotion
        
    @classmethod
    def post(cls):
        try:
            Id = request.form['id']
            title = request.form['title']
            description = request.form['description']

            prompt = f"""Saya memiliki title dan deskripsi postingan sebagai berikut:
                            Title: "{title}"
                            Description: "{description}"

                        Berdasarkan title dan description tersebut, tolong berikan analisis terkait dengan berikut:
                        - Apakah postingan ini dapat dianggap sebagai Hoax? Jawab: true/false
                        - Apakah sentiment dari postingan ini ambigous atau tidak? Jawab: true/false
                        - Apakah terdapat unsur sara atau ujaran kebencian dalam postingan ini? Jawab: sara/ujaran kebencian/false

                        Jawab dengan format:
                        hoax: '' - ambigous: '' - emotion: ''
                        """
                        
            hoax, ambigous, emotion = PredictionScrappingResource.parsing(prediction.predict(prompt))
            data = {
                'label' : hoax,
                'is_ambiguous' : ambigous,
                'news_emotion' : emotion
            }
            
            send = PredictionScrappingResource.upToApi(Id, data)
            return {
                'status' : send,
            }
            
        except Exception as error:
            return {
                'status' : 500,
                'error' : f'{error}'
            }