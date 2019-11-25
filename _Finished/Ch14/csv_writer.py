import csv, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('Workfiles/writer_output.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['One','Two', 'Three', 'Four'])
    writer.writerow(['Helllo, world', 'Ayy lmao', 15])
    writer.writerow([1, 3.1415, 420])

