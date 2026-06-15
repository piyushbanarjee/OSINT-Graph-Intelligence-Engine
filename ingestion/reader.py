import fitz
import pathlib

def read_pdf(filepath):
    doc = fitz.open(filepath)

    for page in doc:
        content = page.get_text()
        return content
        

def read_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        return content

def AutoFileReader(filepath):
    Path = pathlib.Path(filepath)
    filename = Path.name
    type = Path.suffix
    if type == ".txt":
        content =read_txt(filepath)
    elif type == ".pdf":
        content = read_pdf(filepath)
    return filename, content


if __name__ == "__main__":
    pass