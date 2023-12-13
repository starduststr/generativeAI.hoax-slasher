from flask import Flask
from flask_restful import Resource, Api

from resources.PredictionScrappingResource import PredictionScrappingResource
from resources.PredictionUrlResource import PredictionUrlResource
from resources.PredictionTitleDescriptionResource import PredictionTitleDescriptionResource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world '}

api.add_resource(HelloWorld, '/')
api.add_resource(PredictionScrappingResource, '/prediction')
api.add_resource(PredictionUrlResource, '/prediction/url')
api.add_resource(PredictionTitleDescriptionResource, '/prediction/titledescription')

if __name__ == '__main__':
    app.run(debug=True)