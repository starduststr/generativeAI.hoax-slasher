from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request

class PredictionUrlResource(Resource):
    @classmethod
    def post(cls):
        try:
            Id = request.form['id']
            url = request.form['url']

            prompt = f"""Saya memiliki link url postingan sebagai berikut
                       "{url}
                        
                        Url tersebut termasuk ke dalam sentiment Hoax atau Bukan Hoax. Anda cukup jawab hoax atau bukan boax:
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