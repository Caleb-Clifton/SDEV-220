"""
Name: Caleb Clifton
File name: vehicle_app.py
Description: This program defines a Vehicle superclass and an Automobile subclass.
             It accepts user input for an car verhicle type and displays the information
             in a readable format.
Variables:
vehicle_type - string representing the type of vehicle (set to "Car")
year         - string representing the year of the automobile
make         - string representing the manufacturer of the automobile
model        - string representing the model of the automobile
doors        - string representing the number of doors (2 or 4)
roof         - string representing the type of roof (solid or sun roof)
"""

# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Main program
def main():
    # Vehicle type is always "Car" for this app
    vehicle_type = "Car"

    # User input
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roof (solid or sun roof): ")

    # Create Automobile object
    user_car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output
    print("\nVehicle Information:")
    print(f"Vehicle type: {user_car.vehicle_type}")
    print(f"Year: {user_car.year}")
    print(f"Make: {user_car.make}")
    print(f"Model: {user_car.model}")
    print(f"Number of doors: {user_car.doors}")
    print(f"Type of roof: {user_car.roof}")


# Run the program
if __name__ == "__main__":
    main()