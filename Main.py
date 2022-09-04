import csv

from Package import Package

with open('Packages.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        zipcode = row[3]
        deadline = row[4]
        package_weight = row[5]
        delivery_status = row[6]
        notes = row[7]


        package = Package(package_id, address, city, zipcode, deadline, package_weight, delivery_status, notes)
        print(package)
