import fitz


def replace_field_text(pdf_path: str,
                       output_path: str,
                       page_number: int,
                       field_bbox: fitz.Rect,
                       new_text: str,
                       fontfile:str,
                       fontsize: float = 5,
                       line_height: float = 1.2):

    doc = fitz.open(pdf_path)
    page = doc[page_number]
    text = page.get_textbox(field_bbox)
    print(text)
    page.draw_rect(field_bbox, color=(1,1,1), fill=(1,1,1), width=0)
    page.insert_font(fontname="chineze", fontfile=fontfile)
    text_to_insert = text + '\n' + new_text
    result = page.insert_textbox(field_bbox, text_to_insert, fontname='chineze', fontsize=fontsize, lineheight=line_height)
    print(result)
    doc.save(output_path)
    doc.close()



if __name__ == "__main__":

    pdf_in  = "СМГС-2015 (2).pdf"
    pdf_out = "СМГС-2015 (2)_edited.pdf"

    field_3 = fitz.Rect(314.61, 89.73, 570, 200)
    field_4_1 = fitz.Rect(48.52, 124.95, 305.5, 139)
    field_4_2 = fitz.Rect(48.52, 144.95, 310, 165)
    field_5 = fitz.Rect(15.65, 189, 258.50, 205.09)
    field_25 = fitz.Rect(283.30, 677.69, 521.75, 710)
    replace_field_text(pdf_path=pdf_in,
                       output_path=pdf_out,
                       page_number=0,
                       field_bbox=field_3,
                       new_text="中国段铁路运输委托中铁国际多式联运有限公司（CRIMT）代理 委托中铁国际多式联运有限公司（031）负责转关",
                       fontfile="font/static/NotoSansSC-SemiBold.ttf",
                       line_height=1)

