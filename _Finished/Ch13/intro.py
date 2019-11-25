from PyPDF2 import PdfFileReader as PdfReader, PdfFileWriter as PdfWriter

pdf_obj = open('Ch13/meetingminutes.pdf', 'rb')
pdf_reader = PdfReader(pdf_obj)
print(pdf_reader.numPages) # Output: 19

page_obj = pdf_reader.getPage(0)
print(page_obj.extractText())