import csv

filename = 'realestate.csv'

with open (filename) as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        print(row[0],row[1])