"""
A big pharmaceutical company in your home town has a lot of different cars and other vehicles.
So far they have been using books to keep track of them, but now they'd like to have a computer program to do this.

Each vehicle has these attributes:
brand
model
kilometers done so far
general service date

The program should allow user to:

see a list of vehicles the company has
edit kilometers and the general service date for each vehicle
add new vehicle
Use TXT file to store data about vehicles in.
When you finish, push your code on GitHub and share it on the forum.
"""

class vehicle:
    def __init__(self, brand, model, kilometers_so_far, service_date):
        self.brand = brand
        self.model = model
        self.kilometers_so_far = kilometers_so_far
        self.service_date = service_date

    def get_vehicle_name(self):
        return self.brand + " " + self.model


def list_all_vehicle(vehicles):
    for index, car in enumerate(vehicles):
        print "Number: " + str(index)  # index is an order number of the contact object in the contacts list
        print "Vehicle brand and model: " + car.get_vehicle_name()
        print "Kilometers: " + car.kilometers_so_far
        print "General service date: " + car.service_date
        print ""  # empty line

    if not vehicles:
        print "You don't have any vehicles in your list."




# edit kilometers and service date
def edit_kilometers(vehicles):
    print "Select the number of the vehicle you'd like to edit:"

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_vehicle_name()

    print ""  # empty line
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_kilometers_so_far = raw_input("Please enter a new kilometers for %s: " % selected_vehicle.get_vehicle_name())
    selected_vehicle.kilometers_so_far = new_kilometers_so_far

    print ""  # empty line
    print "Kilometers are updated."
    # ... you can do the same for other fields.

def edit_service_date(vehicles):
    print "Select the number of the vehicle you'd like to edit:"

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_vehicle_name()

    print ""  # empty line
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_service_date = raw_input("Please enter a new service date for %s: " % selected_vehicle.get_vehicle_name())
    selected_vehicle.service_date = new_service_date

    print ""  # empty line
    print "Service date is updated."
    # ... you can do the same for other fields.



# delete item from a list
def delete_vehicle(vehicles):
    print "Select the number of the vehicle you'd like to delete:"

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_vehicle_name()

    print ""  # empty line
    selected_id = raw_input("What vehicle would you like to delete? (enter ID number): ")
    selected_vehicles = vehicles[int(selected_id)]

    vehicles.remove(selected_vehicles)
    print ""  # empty line
    print "Vehicle was successfully removed from your contact list."



# adding new vehicle to the list
def add_new_vehicle(vehicles):
    brand = raw_input("Please enter brand of vehicle: ")
    model = raw_input("Please enter model of the vehicle: ")
    kilometers = raw_input("Please enter vehicle's kilometers so far: ")
    service = raw_input("Please enter vehicle's general service date: ")

    new = vehicle(brand=brand, model=model, kilometers_so_far=kilometers, service_date=service)
    vehicles.append(new)

    print ""  # empty line
    print new.get_vehicle_name() + " was successfully added to your vehicle list."



def main():
    print "Welcome to Pharmaceutical company and our vehicles"

    # let's add some contacts in our contact list so it's not empty
    alfa_romeo = vehicle(brand="Alfa Romeo", model="Stelvio SUV", kilometers_so_far="120 000", service_date="12.07.2017.")
    aston_martin = vehicle(brand="Aston Martin", model="V8 Vantage", kilometers_so_far="3 000", service_date="09.08.2017.")
    audi_r8 = vehicle(brand="Audi", model="R8 Spyder", kilometers_so_far="500", service_date="15.04.2018.")
    vehicles = [alfa_romeo, aston_martin, audi_r8]

    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See list of vehicles"
        print "b) Edit kilometers"
        print "c) Edit general service date"
        print "d) Delete a vehicle"
        print "e) Add new vehicle"
        print "f) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, d e or f): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_vehicle(vehicles)
        elif selection.lower() == "b":
            edit_kilometers(vehicles) #add_new_contact(contacts)
        elif selection.lower() == "c":
            edit_service_date(vehicles)
        elif selection.lower() == "d":
            delete_vehicle(vehicles)
        elif selection.lower() == "e":
            add_new_vehicle(vehicles)
        elif selection.lower() == "f":
            print "Thank you for using vehicle manager. Goodbye!"
            def write_all_vehicle(vehicles):
                for index, car in enumerate(vehicles):
                    carList.write("Number: " + str(index) + "\n")  # index is an order number of the contact object in the contacts list
                    carList.write("Vehicle brand and model: " + car.get_vehicle_name() + "\n")
                    carList.write("Kilometers: " + car.kilometers_so_far + "\n")
                    carList.write("General service date: " + car.service_date + "\n")
                    carList.write("" + "\n")  # empty line
                if not vehicles:
                    print "You don't have any vehicles in your list."
            carList = open("vehicles.txt", "w")
            data = write_all_vehicle(vehicles)
            carList.write(str(data))
            carList.close()
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":
    main()