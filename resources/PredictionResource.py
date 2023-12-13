import os
import vertexai
from vertexai.language_models import TextGenerationModel

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "durable-boulder-407913-0a0904bf432a.json"

class PredictionResources:
    @classmethod
    def predict(cls, prompt):
        vertexai.init(project="durable-boulder-407913", location="asia-southeast1")
        parameters = {
            "candidate_count": 1,
            "max_output_tokens": 1024,
            "temperature": 0.2, # 1 lebih creative, 0 presisi
            "top_p": 0.8,
            "top_k": 40
        }
        model = TextGenerationModel.from_pretrained("text-bison")
        response = model.predict(
            prompt,
            **parameters
        )
        
        return response.text
 
 
        
    