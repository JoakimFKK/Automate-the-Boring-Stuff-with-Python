import csv, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('this_file_doesnt_exists.tsv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
    writer.writerow(['Apples', 'oranges', 'grapes'])
    writer.writerow(['123', '123', '1312'])