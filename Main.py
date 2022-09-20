#Abisola Oseni 001345382
import csv
import datetime

import Truck
from Package import Package
from Hash_Table import HashTable


distance_list=[]
address_list=[]

#Create hash table
package_hash_table = HashTable()

# Space-Time Complexity: O(N)
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

# Space-Time Complexity: O(N)
# Loading the package data and reading it from the csv file
with open('Distances.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        distance_list.append(row)

# Space-Time Complexity: O(N)
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

# Space-Time Complexity: O(N)
# Method that accepts an address and returns the index of address in the address list
def address_index(address):
    for row in address_list:
        if address in row[2]:
            return int(row[0])


# Space-Time Complexity: O(1)
# Method that accepts a starting and ending address and returns the distance from the distance table
def distance_between_addresses(starting_address, ending_address):

    starting_index = address_index(starting_address)
    ending_index = address_index(ending_address)

    if ending_index > starting_index:

        distance = float(distance_list[ending_index][starting_index])
    else:
        distance = float(distance_list[starting_index][ending_index])
    return distance

# pass it a truck and it will deliver all the packages in that truck
# look at EOD package info and general package info to 'manually' load the trucks

# Truck Object #1
truck1 = Truck.Truck(1, [15, 14, 13, 19, 16, 20, 24, 37, 29, 30, 31, 34, 40], datetime.timedelta(hours=8, minutes=5))
# Truck Object #2
truck2 = Truck.Truck(2, [1, 11, 12, 22, 3, 18, 23, 36, 38, 6, 25], datetime.timedelta(hours=9, minutes=5))
# Truck Object #3
truck3 = Truck.Truck(3,  [26, 32, 2, 4, 5, 7, 8, 9, 17, 33, 35, 28, 27, 21, 39, 10], datetime.timedelta(hours=10, minutes=30))

#Greedy Algorithm
# Space-Time Complexity: O(N)
#Finds the closest address and the package ID that is closest to that address
#Returns the closest address, package ID closest to that address and distance between the current address and the next address
def distance_from_address(address1, package_list):
    min = 1000
    next_address = ''
    next_id = 0
    for package_id in package_list:
        package = package_hash_table.lookup(package_id)
        address2 = package.address
        distance = distance_between_addresses(address1, address2)
        if distance < min:
            min = distance
            next_address = address2
            next_id = package_id
    return next_address, next_id, min

#Algorithm to deliver packages
# Space-Time Complexity: O(N)
#Takes a truck and the start time, which is when the truck leaves the hub
#Passes the packages to the truck through the distance_from_address function to find the address to the closest package
#That closest package will be delivered next and the status of the address will be changed and the delivery time will be assigned
#keeps track of miles and time but only returns miles
def deliverpackages(truck):
    time = truck.start_time
    address_from = "4001 South 700 East"
    miles = 0
    while(len(truck.package_list) > 0):
        visited, package_id, package.distance = distance_from_address(address_from, truck.package_list)
        if package_id == 40:
            pass
        miles = miles + package.distance
        delivery_time_seconds = datetime.timedelta(seconds=(package.distance/18)*60*60)
        time = time + delivery_time_seconds

        delivered = package_hash_table.lookup(package_id)
        delivered.delivery_time = time
        delivered.delivery_status = 'delivered'
        address_from = visited
        truck.package_list.remove(package_id)
    return miles, time

#Determine the start time for each truck
# Space-Time Complexity: O(1)
def get_truck_start_time_for_package(package_id):
    if package_id in truck1.original_package_list:
        return truck1.start_time
    elif package_id in truck2.original_package_list:
        return  truck2.start_time
    else:
        return truck3.start_time


#Then call the deliver packages method and pass in the truck id and time the truck left the hub (start time) which will return the number of miles each truck traveled
truck1_miles, truck1_finish_time = deliverpackages(truck1)
truck2_miles, truck2_finish_time = deliverpackages(truck2)

truck3.start_time = truck1_finish_time
pkg9 = package_hash_table.lookup(9)
pkg9.address = "410 S State St"
pkg9.city = "Salt Lake City"
pkg9.state = "UT"
pkg9.zipcode = "84111"

truck3_miles, truck3_finish_time = deliverpackages(truck3)

#total miles is derived from summing up the mileage from all three trucks
total_miles = truck1_miles + truck2_miles +truck3_miles

# User Interface
# Space-Time Complexity: O(N)
print("Welcome to WGUPS - The total mileage is: " + str(total_miles))
print("Please make a selection from the following options:")
print("1. Display the status of all packages")
print("2. Look up a package by ID number")
print("3. Exit")
selection = input("Please enter your selection: ")
if selection == '1':
    time = input("Enter the time HH:mm")
    hours, minutes = time.split(":")
    requested_time = datetime.timedelta(hours=int(hours), minutes=int(minutes))
    for i in range(1, 41):
        pkg = package_hash_table.lookup(i)
        start_time = get_truck_start_time_for_package(i)
        print(pkg.print_status_for_time(requested_time, start_time))

if selection == '2':
    package_id = input("Enter package ID")
    print(package_hash_table.lookup(int(package_id)))