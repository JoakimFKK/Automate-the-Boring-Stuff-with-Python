import csv, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

csv_file = open("Workfiles/example.csv")
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)
print(csv_data)
"""Output:
    [['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'], ['4/6/2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'], ['4/10/2014 2:07', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'], ['4/10/2014 2:40', 'Strawberries', '98']]
"""

print(csv_data[0][0]) # 4/5/2014 13:34
print(csv_data[0][1]) # Apples
print(csv_data[0][2]) # 73
print(csv_data[1][1]) # Cherries