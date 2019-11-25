from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_reader = PdfFileReader(open("Ch13/encrypted.pdf", 'rb'))
print(pdf_reader.isEncrypted) # Output: True
pdf_reader.decrypt("rosebud")
print(pdf_reader.isEncrypted) # Output: True
print(pdf_reader.getPage(0).extractText()) # Output: [TEXT FROM PDF]