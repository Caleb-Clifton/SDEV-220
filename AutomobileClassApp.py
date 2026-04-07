"""
Name: Caleb Clifton
File name: vehicle_app.py
Description: This program defines a Vehicle superclass and an Automobile subclass.
             It accepts user input for an car verhicle type and displays the information
             in a readable format.
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
    # Vehicle type is always "car" for this app
    vehicle_type = "car"

    # User input
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roof (solid or sun roof): ")

    # Create Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output
    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")


# Run the program
if __name__ == "__main__":
    main()