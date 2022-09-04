class Package:
    def __init__(self, package_id, address, city, zipcode, deadline, package_weight, delivery_status, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.notes = notes
        self.delivery_time = None
        self.distance = 0
    def __str__(self):
        return f'{self.package_id}\t {self.address}\t {self.city}\t {self.zipcode}\t {self.deadline}\t {self.package_weight}\t {self.delivery_status}\t {self.notes}'

    def isDelivered(self):
        return self.delivery_time is not None

    def isNotDelivered(self):
        return not self.isDelivered()
