#region

import openpyxl, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

print(tuple(sheet['A1':'C3']))
"""Output:
    ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
"""
for row in sheet['A1':'C3']:
    for cell_obj in row:
        print(cell_obj.coordinate, cell_obj.value)
    print("--- END OF ROW ---")
"""Output:
    A1 2015-04-05 13:34:02
    B1 Apples
    C1 73
    --- END OF ROW ---
    A2 2015-04-05 03:41:23
    B2 Cherries
    C2 85
    --- END OF ROW ---
    A3 2015-04-06 12:46:51
    B3 Pears
    C3 14
    --- END OF ROW ---
"""
#endregion


import openpyxl, os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active # get_active_sheet
print(sheet['B']) # (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
for cell_obj in sheet['B']:
    print(cell_obj.value)
"""Output:
    Apples
    Cherries
    Pears
    Oranges
    Apples
    Bananas
    Strawberries
"""
for cell_obj in sheet[1]:
    print(cell_obj.value)
"""Output:
    2015-04-05 13:34:02
    Apples
    73
"""

