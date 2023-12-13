from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request

class PredictionTitleDescriptionResource(Resource):
    @classmethod
    def post(cls):
        try:
            title = request.form['title']
            description = request.form['description']

            prompt = f"""Saya memiliki title dan deskripsi postingan sebagai berikut:
            
                            Title: "{title}"
                            Description: "{description}"

                        Berdasarkan title dan description tersebut apakah termasuk ke dalam sentiment Hoax atau Bukan Hoax. Anda cukup jawab hoax atau bukan boax:
                        """
            
            return {
                'status' : 200,
                'data': {
                    'prediction' : prediction.predict(prompt)
                }
            }
            
        except Exception as error:
            return {
                'status' : 500,
                'error' : f'{error}'
            }