from resources.PredictionResource import PredictionResources as prediction
from flask_restful import Resource
from flask import request

class PredictionImageUrlResource(Resource):
    
    @classmethod
    def parsing(cls, data):
        data_list = data.split(" - ")

        judul_berita = data_list[0].split(":")[1]
        deskripsi_berita = data_list[1].split(":")[1]
        url_gambar = data_list[2].split("a:")[1]
        label = data_list[3].split(":")[1]
        
        print(judul_berita, deskripsi_berita, url_gambar, label)
        return judul_berita, deskripsi_berita, url_gambar, label
    
    @classmethod
    def post(cls):
        try:
            Id = request.form['id']
            url = request.form['url']

            prompt = f"""Hai...
                            Tolong bantu saya untuk menganalisa berita yang ada dalam link berikut ini :

                            {url}

                            Lalu tolong analisis isi dari link tersebut apakah mengandung berita hoax atau aktual. 
                            
                            Jawab dengan format seperti berikut untuk mempermudah parsing:
                            Judul berita: isi disini - Deskripsi berita: isi disini - Image url berita: isi disini - Label: Aktual/Hoax
                      """
            predict = prediction.predict(prompt)
            judul_berita, deskripsi_berita, url_gambar, label = PredictionImageUrlResource.parsing(predict)
            return {
                'status' : 200,
                'data' : {
                    'title' : judul_berita,
                    'description' : deskripsi_berita,
                    'image_url' : url_gambar,
                    'label' : label,
                }
                # 'asli': predict
            }
            
        except Exception as error:
            return {
                'status' : 500,
                'error' : f'{error}'
            }