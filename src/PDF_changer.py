import fitz


class Pdf_changer():
    def __init__(self, pdf_path: str, fontsize: int = 6, lineheight: float = 1.0):
        self.doc = fitz.open(pdf_path)
        self.field_3 = fitz.Rect(314.61, 89.73, 570, 200)
        self.field_4_1 = fitz.Rect(48.52, 124.95, 305.5, 139)
        self.field_4_2 = fitz.Rect(48.52, 144.95, 310, 165)
        self.field_5 = fitz.Rect(15.65, 189, 258.50, 205.09)
        self.field_25 = fitz.Rect(283.30, 677.69, 521.75, 710)
        self.fontsize = fontsize
        self.lineheight = lineheight

    def explict_text(self, page: fitz.Page, field: fitz.Rect):
        return page.get_textbox(field)

    def fill_old_field(self, page: fitz.Page, field: fitz.Rect):
        page.draw_rect(field, color=(1, 1, 1), fill=(1, 1, 1), width=0)

    def write_new_text(self, page: fitz.Page, field: fitz.Rect, fontfile: str, new_text: str):
        page.insert_font(fontname="chineze", fontfile=fontfile)
        text = self.explict_text(page, field)
        text_to_insert = text + '\n' + new_text
        page.insert_textbox(field, text_to_insert, fontname='chineze', fontsize=self.fontsize, lineheight=self.line_height)
