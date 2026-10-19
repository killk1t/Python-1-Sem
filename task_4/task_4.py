import csv
with open('fail_csv.csv') as f:
    with open('expensive.csv', 'w', newline='') as d:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(d, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if int(row['price']) >= 100:
                writer.writerow(row)