import csv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue
    csv_rows = []
    with open(csv_filename) as csv_file_obj:
        reader = csv.reader(csv_file_obj)
        for row in reader:
            if reader.line_num == 1:
                continue
            csv_rows.append(row)
    
    with open(f'HeaderRemoved_{csv_filename}', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for row in csv_rows:
            writer.writerow(row)
    