from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request
import requests as reqs


# prediksi dari hasil scrapping -> update ke database
# 	params : - id
# 		     - title
# 		     - description
# 		     - 
	
# 	field : - label (true, false)
# 		    - isAmbigous (true, false)
# 		    - isTraining (true, false)
# 		    - traningDate (date)
# 		    - newsEmotion (ujaran kebencian, sara, etc)

class PredictionTitleDescriptionResource(Resource):
    
    @classmethod
    def upToApi(cls):
        method = "GET"
        url = "https://mfsz3q3f-4100.asse.devtunnels.ms/news"
        params = {"id": 1, "title": "title", "description": "description"}
        response = reqs.request(method, url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(response.status_code)
            
    @classmethod
    def parsing(cls, data):
        data_list = data.split(" - ")

        hoax = data_list[0].split(":")[1]
        ambigous = data_list[1].split(":")[1]
        emotion = data_list[2].split(":")[1]
        
        print(hoax, ambigous, emotion)
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
                        
            hoax, ambigous, emotion = PredictionTitleDescriptionResource.parsing(prediction.predict(prompt))
            return {
                'status' : 200,
                'hoax' : hoax,
                'ambigous' : ambigous,
                'emotion' : emotion
            }
            
        except Exception as error:
            return {
                'status' : 500,
                'error' : f'{error}'
            }