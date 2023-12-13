from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request

class PredictionScrappingResource(Resource):
    def get(self):
        try:
            Id = request.form['id']
            title = request.form['title']
            description = request.form['description']

            prompt = f"""Saya memiliki caption postingan sebagai berikut
                        title : "{title}"
                        isi : "{description}"
                        
                        Kalimat tersebut termasuk ke dalam sentiment Hoax atau Bukan Hoax. jawab dalam format:
                    """
            prompt += """
                         {
                            sentiment: ""
                          }
                        """
            print(prediction.predict(prompt))
            return {
                'prediction' : prediction.predict(prompt)
            }
            
        except Exception as error:
            return {
                'error' : f'{error}'
            }