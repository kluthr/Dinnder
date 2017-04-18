import csv
import random
from place import Place

class CLI(object):

    def __init__(self):
        self.options = []

    def load_places(self, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                place = Place(row)
                self.options.append(place)

    def present_options(self):
        while self.options:
            option = random.choice(self.options)
            option.print_place()
            self.options.remove(option)
            answer = raw_input("Yes or No? ")
            if answer.lower() in ("yes", "y"):
                print "{} is a great choice! Enjoy!".format(option.name)
                exit()
        print "No more options! You are going to starve! :("
        
    @classmethod
    def run(cls):
        cli = cls()
        cli.load_places("places.csv")
        cli.present_options()


if __name__ == "__main__":
    CLI.run()
