import docx, os

def get_text(filename):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)
