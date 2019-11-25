import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active

italic24_font = Font(size=24, italic=True)
comic_sans = Font(name='Comic Sans MS', size=24, bold=True)

sheet['A1'].font = italic24_font
sheet['A1'].value = "Helloworld no space"
sheet['A3'].font = comic_sans
sheet['A3'].value = "What have you brought upon this cursed Kingdom."


wb.save("Ch12/Workfiles/stylingDOTpy styled.xlsx")