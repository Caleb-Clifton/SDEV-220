# Honor Roll App (filename HonorRollApp.py)
# Author: Caleb Clifton
# This program allows users to input student names and their GPA, and then displays what honor roll criteria they meet. 


# Function to determine honor roll status based on GPA
def grade_test(GPA):
    if GPA >= 3.5:
        return "the Dean's List and the Honor Roll"
    elif GPA >= 3.25:
        return "the Honor Roll"
    else:
        return "None"
    
# Main function to run the Honor Roll App
def main():
    print("Welcome to the Honor Roll App!")
    # Loop to continuously accept student information until the user decides to quit
    while True:
        lastName = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if lastName == 'ZZZ':
            break
        firstName = input("Enter the student's first name: ")
        # Try-except block to handle invalid input for GPA to avoid crashing the program
        try:
            GPA = float(input("Enter the student's GPA: ")) 
        except ValueError:
            print("Invalid input for GPA. Please enter a numeric value.")
            continue
        # Call the grade_test function to determine the honor roll status and print the result
        honor_roll_status = grade_test(GPA)
        if honor_roll_status != "None":
            print(f"{firstName} {lastName} has made {honor_roll_status}.")
        else:
            print(f"{firstName} {lastName} has not made the honor roll.")
        print()  # Print a blank line for better readability
    print("Thank you for using the Honor Roll App!")

if __name__ == "__main__":
    main()