import os

from tqdm import tqdm
import pytesseract
import pdf2image
import pdftotext

SYLLABI_PATH = "./syllabi"
SYLLABI_TEXT_PATH = "./syllabi_text"


def convert_pdf_to_text(pdf_path, pages="all"):
    """
    Converts a pdf to a string. Little formatting, but can choose which pages to convert
    :param pdf_path: Pages to convert
    :param pages:
    :return:
    """
    images = pdf2image.convert_from_path(pdf_path, dpi=400)

    if pages == "all":
        pass
    else:
        images = [images[a] for a in pages]

    to_ret = ""
    for page in images:
        to_ret += pytesseract.image_to_string(page)

    return to_ret


if __name__ == '__main__':
    """
    Converts all of the syllabi to text
    """
    for file in tqdm(os.listdir(SYLLABI_PATH)):
        file_name = file[:file.index(".")]
        with open(f"{SYLLABI_PATH}/{file}", "rb") as syllabus:
            try:
                pdf = pdftotext.PDF(syllabus)
            except pdftotext.Error:
                print(f"{file} generated this error")
            text = "\n\n".join(pdf)
        with open(f"{SYLLABI_TEXT_PATH}/{file_name}.txt", "w") as f:
            f.write(text)
