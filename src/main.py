from PDF_changer import Pdf_changer
from api.models import JsonModel
from fastapi import FastAPI


app = FastAPI()


@app.post("/api/pdf_changer")
async def change_pdf(json: JsonModel):
    for file in json["files"]:
        pdf_changer = Pdf_changer(file, 'font/static/NotoSansSC-SemiBold.ttf')
        pdf_changer.change_all(
            text_for_field_3=json["text_for_field_3"],
            text_for_field_4_1=json["text_for_field_4_1"],
            text_for_field_4_2=json["text_for_field_4_2"],
            text_for_field_5=json["text_for_field_5"],
            text_for_field_25=json["text_for_field_25"]
        )


