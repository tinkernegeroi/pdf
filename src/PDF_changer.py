import fitz
import random

class Pdf_changer():
    def __init__(self,
                 pdf_path: str,
                 fontfile: str,
                 fontsize: int = 6,
                 lineheight: float = 1.0
    ):
        self.doc = fitz.open(pdf_path)
        self.field_3 = fitz.Rect(314.61, 89.73, 570, 200)
        self.field_4_1 = fitz.Rect(48.52, 124.95, 305.5, 139)
        self.field_4_2 = fitz.Rect(48.52, 144.95, 310, 165)
        self.field_5 = fitz.Rect(15.65, 189, 258.50, 205.09)
        self.field_25 = fitz.Rect(283.30, 677.69, 521.75, 710)
        self.fontsize = fontsize
        self.fontfile = fontfile
        self.lineheight = lineheight


    def change_all(self, text_for_field_3: str | None, text_for_field_4_1: str | None, text_for_field_4_2: str | None, text_for_field_5: str | None, text_for_field_25: str | None):
        for n in range(0, len(self.doc), 1):
            page = self.doc[n]

            if text_for_field_3 is not None:
                text_from_field_3 = self.extract_text(page, self.field_3)
                text_to_insert_3 = text_for_field_3 + '\n' + text_from_field_3
                self.fill_old_field(page, self.field_3)
                self.write_new_text(page, self.field_3, self.fontfile, text_to_insert_3)

            if text_for_field_4_1 is not None:
                text_from_field_4_1 = self.extract_text(page, self.field_4_1)
                text_to_extract_4_1 = text_for_field_4_1 + '\n' + text_from_field_4_1
                self.fill_old_field(page, self.field_4_1)
                self.write_new_text(page, self.field_4_1, self.fontfile, text_to_extract_4_1)

            if text_for_field_4_2 is not None:
                text_from_field_4_2 = self.extract_text(page, self.field_4_2)
                text_to_extract_4_2 = text_from_field_4_2 + '/' + text_for_field_4_2
                self.fill_old_field(page, self.field_4_2)
                self.write_new_text(page, self.field_4_2, self.fontfile, text_to_extract_4_2)

            if text_for_field_5 is not None:
                text_from_field_5 = self.extract_text(page, self.field_5)
                text_to_extract_5 = text_from_field_5 + '/' + text_for_field_5
                self.fill_old_field(page, self.field_5)
                self.write_new_text(page, self.field_5, self.fontfile, text_to_extract_5)

            if text_for_field_25 is not None:
                text_from_field_25 = self.extract_text(page, self.field_25)
                text_to_extract_25 = text_from_field_25 + '/' + text_for_field_25
                self.fill_old_field(page, self.field_25)
                self.write_new_text(page, self.field_25, self.fontfile, text_to_extract_25)


        self.doc.save("1" + str(random.randint(1,6)) + ".pdf")
        self.doc.close()


    def extract_text(self, page: fitz.Page, field: fitz.Rect):
        return page.get_textbox(field)


    def fill_old_field(self, page: fitz.Page, field: fitz.Rect):
        page.draw_rect(field, color=(1, 1, 1), fill=(1, 1, 1), width=0)


    def write_new_text(self,
                       page: fitz.Page,
                       field: fitz.Rect,
                       fontfile: str,
                       text: str
    ):
        page.insert_font(fontname="chineze", fontfile=fontfile)
        res = page.insert_textbox(field, text, fontname='chineze', fontsize=self.fontsize, lineheight=self.lineheight)
        while res < 0:
            self.fontsize -= 1
            res = page.insert_textbox(field, text, fontname='chineze', fontsize=self.fontsize, lineheight=self.lineheight)
