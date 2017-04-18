class Place(object):

    def __init__(self, data):
        self.name = data['Name']
        self.speed = data['Speed']
        self.health = data['Healthiness']
        self.price = data['Price']
        self.flavor = data['Flavor']
        self.delivers = data['Delivers']
        self.fee = data['PickupFee']
        self.bar = data['Bar']

    def print_place(self):
        print "{}{}".format(" " * (12 - (len(self.name)/2)), self.name)
        print "{}Speed:{}".format(" " * 9, self.speed)
        print "{}Health:{}".format(" " * 8, self.health)
        print "{}Price:{}".format(" " * 9, self.price)
