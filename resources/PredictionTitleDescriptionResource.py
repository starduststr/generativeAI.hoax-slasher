from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request


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

                        Contoh jawaban:
                        hoax: false, ambigous: true, emotion: false
                        """
            return {
                'status' : 200,
                'prediction' : prediction.predict(prompt)
            }
            
        except Exception as error:
            return {
                'status' : 500,
                'error' : f'{error}'
            }