import csv
import datetime

import Truck
from Package import Package
from Hash_Table import HashTable


distance_list=[]
address_list=[]

#Create hash table
package_hash_table = HashTable()

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

# Insert data into hash table
        package_hash_table.insert(package_id, package)


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

# pass it a truck and it will deliver all the packages in that truck
# look at EOD package info and general package info to 'manually' load the trucks

# Truck Object #1
truck1 = Truck.Truck(1, [1, 10, 11, 12, 21, 22, 23, 24, 26, 37, 29, 30, 31, 34], datetime.timedelta(hours=8, minutes=5))
# Truck Object #2
truck2 = Truck.Truck(2, [6, 14, 15, 19, 13, 16, 3, 18, 20, 36, 38, 39, 40], datetime.timedelta(hours=9, minutes=5))
# Truck Object #3
truck3 = Truck.Truck(3,  [25, 32, 2, 4, 5, 7, 8, 9, 17, 33, 35, 28, 27], datetime.timedelta(hours=10, minutes=5))

#Greedy Algorithm
def distance_from_address(address1, package):
    min = 1000
    next_address = ''
    next_id = 0
    for package_id in package:
        package = package_hash_table.lookup(package_id)
        # print(packages)
        address2 = package.address
        # print(address2)
        distance = distance_between_addresses(address1, address2)
        if distance < min:
            min = distance
            next_address = address2
            next_id = package_id
    return next_address, next_id, min

#Algorithm to deliver packages
def deliverpackages(truck, starttime):
    hour, minute, second = starttime.split(":")
    time = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
    address_from = "4001 South 700 East"
    miles = 0
    for package_id in truck.package_list[:]:
        visited, package_id_delivered, distance_traveled = distance_from_address(address_from, truck.package_list)
        miles = miles + distance_traveled
        delivery_time = (distance_traveled/18)*60*60
        dts = datetime.timedelta(seconds=delivery_time)
        time = time + dts

        delivered = package_hash_table.lookup(package_id_delivered)
        delivered.delivery_time = time
        delivered.status = 'delivered'
        address_from = visited
        truck.package_list.remove(package_id_delivered)
    return miles

truck1_miles = deliverpackages(truck1, '08:05:00')
truck2_miles = deliverpackages(truck2, '09:05:00')
truck3_miles = deliverpackages(truck3, '10:05:00')

#total miles from all three trucks
total_miles = truck1_miles + truck2_miles +truck3_miles
print(total_miles)
