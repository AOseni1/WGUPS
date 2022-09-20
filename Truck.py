class Truck:

    def __init__(self, truck_id, package_list, start_time):
        self.truck_id = truck_id
        self.package_list = package_list
        self.start_time = start_time
        self.original_package_list = package_list.copy()
    def total_mileage(self):
        mileage = 0
        for package in self.package_list:
            mileage += package.distance

        return mileage
