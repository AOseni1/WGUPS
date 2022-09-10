import csv

from Package import Package


distance_list=[]
address_list=[]

# Loading the package data and reading it from the csv file
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

# Creating the package object
        package = Package(package_id, address, city, zipcode, deadline, package_weight, delivery_status, notes)
        # print(package)

# Loading the package data and reading it from the csv file
with open('Distances.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        distance_list.append(row)

# print(distance_list)

# Loading the address data and reading it from the csv file
with open('Addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        index = row[0]
        address_name = [1]
        address = row[2]
        city = row[3]
        state = row[4]
        zipcode = row[5]
        address_list.append(row)


# Method that accepts an address and returns the index of address in the address list
def address_index(address):
    for row in address_list:
        if address in row[2]:
            return int(row[0])

# print(address_index("3060 Lester St"))
# Method that accepts a starting and ending address and returns the distance from the distance table
def distance_between_addresses(starting_address, ending_address):
    starting_index = address_index(starting_address)
    ending_index = address_index(ending_address)
    # add an if statement to determine if ending index is greater than starting index
    # if not starting_index or not ending_index:
    #     return "Unable to find the distance between the addresses"
    if ending_index > starting_index:
        distance = float(distance_list[ending_index][starting_index])
    else:
        distance = float(distance_list[starting_index][ending_index])
    return distance


print((distance_between_addresses('2010 W 500 S', '3060 Lester St' )))
# print(address_list)