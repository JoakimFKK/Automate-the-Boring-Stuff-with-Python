import openpyxl
import os

def update_spreadsheet():
    """Process:
        1)  Get Excel(Workbook) file
        2)  Get the active sheet.
        3)  Make dictionary for changes.
        4)  Loop through the sheet, checking if the value in column A(X) is in the dictionary.
        4a) If yes, change the value of B(X) to the value of the key.
        4b) If no, nothing happens and the program goes to the next cell.
        5)  The Workbook is saved as "NEW_ProduceSale.xlsx" in the same folder where this file is located.
    """
    wb = openpyxl.load_workbook(workfile_path)
    active_sheet = wb.active
    produce_items = { 'Celery': 1.19, 'Garlic': 3.07, 'Lemon': 1.27 }
    # Loop through rows
    for i in range(2, active_sheet.max_row + 1):
        if active_sheet['A' + str(i)].value in produce_items:
            active_sheet['B' + str(i)].value = produce_items[active_sheet['A' + str(i)].value]

    wb.save("NEW_PrduceSale.xlsx")

if __name__ == "__main__":
    """Minor preference changes, but entirely unnecessary."""
    os.chdir(os.path.dirname(os.path.realpath(__file__))) # C:\Users\joak\Documents\repositories\py_automate\Ch12
    workfile_path = os.path.join(os.getcwd(), 'Workfiles\\produceSales.xlsx')
    update_spreadsheet()