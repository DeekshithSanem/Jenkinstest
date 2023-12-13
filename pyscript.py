import csv

with open("incsv.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))