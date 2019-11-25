import csv, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

csv_file = open("Workfiles/example.csv")
reader = csv.reader(csv_file)
for row in reader:
    print(f"Row #{reader.line_num} | {str(row)}")
"""Output:
    Row #1 | ['4/5/2014 13:34', 'Apples', '73']
    Row #2 | ['4/5/2014 3:41', 'Cherries', '85']
    Row #3 | ['4/6/2014 12:46', 'Pears', '14']
    Row #4 | ['4/8/2014 8:59', 'Oranges', '52']
    Row #5 | ['4/10/2014 2:07', 'Apples', '152']
    Row #6 | ['4/10/2014 18:10', 'Bananas', '23']
    Row #7 | ['4/10/2014 2:40', 'Strawberries', '98']
"""