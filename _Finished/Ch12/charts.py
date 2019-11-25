import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.Workbook()
ws = wb.active
for i in range(1, 11):
    ws.append([i])

values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)
chart = BarChart()
chart.add_data(values)

ws.add_chart(chart, "E15")
"""By default the top-left corner of a chart is anchored to cell E15 and the size is 15 x 7.5 cm (approximately 5 columns by 14 rows). This can be changed by setting the anchor, width and height properties of the chart. The actual size will depend on operating system and device. Other anchors are possible see openpyxl.drawing.spreadsheet_drawing for further information.
"""
wb.save("Ch12/Workfiles/Chart.xlsx")