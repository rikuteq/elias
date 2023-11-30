# Lists to hold plates and credit card numbers
plates = []
cc_numbers = []

# Function for registering a vehicle
def register_vehicle():
    # If there are no spaces left in the lot, prints the lot is full
    if len(plates) >= 50:
        print(f"The parking lot is full.")
        input("Please press enter to continue...")
        # If there are spaces in the lot, run the program
    else:
        print(f"The parking lot has spaces for your vehicle.")
        # Ask for the plate number
        plateNum = str(input(f"Enter your plate number: "))
        # If the plate number is already registered run this program
        if plateNum in plates:
            # Inform that the vehicle is already registered
            print(f"{plateNum} is already registered")

        # If the plate is not yet registered run this program
        elif plateNum not in plates:
            # Add the plate number to the list of plates that are registered
            plates.append(plateNum)
            # Ask for credit card number
            cc = str(input(f"Enter your Credit Card Number ($4.00 charge): "))
            # Add credit card number to the list of credit card numbers
            cc_numbers.append(cc)
            with open("vehicles.txt","w") as wf:   # Overwrites the text file and makes it completely blank
                wf.write("")
            for plate in plates:
                with open("vehicles.txt","a") as f:   # Appends text to the text file 
                    if plate not in open("vehicles.txt","r").read():    # if the plate number is not already in the file, then it adds it (stops repeating plates)
                        f.write(f"{plate}" "\n")
            
            # Successfully registered the vehicle and is in the parking lot
            print(f"Thank you, your plate {plateNum} has been added to the lot.")
            print(plates)
        input("Please press enter to continue...")

# Function to check password for administrative permissions
def check_password():
    password = input("Enter your Password: ")  # Asks user to enter password
    if password != 'password': # If the password entered is not equal to 'password', then prints Incorrect and exits
        print("Password is incorrect!")
        exit() # Exits program if password is incorrect

# Function to verify vehicle registration
def verify_vehicle():
    check_password()
    verify_plate = input("Enter your plate number to verify: ") # Asks user for input to enter their plate number
    if verify_plate in plates: # If the number inputed is in the list for plates, then the vehicle is registered otherwise its not
        print(f"The vehicle with plate# {verify_plate} is registered in the lot.")
    else:
         print("Vehicle is NOT registered.")              
    input("Please press enter to continue...")

# Function to remove vehicles from the lot via admin privileges 
def remove_vehicle():
    check_password()
    remove_plate = input("Enter a plate number: ") # Asks for user to input the plate number for removal
    
    pos = plates.index(remove_plate) # Grabs the index number in the list of the item remove_plate
    del cc_numbers[pos] # Removes cc equivalent of plate by removing same index number
    
    if remove_plate in plates:
        plates.remove(remove_plate) # Removes the inputted plate from the plates list
    else:
        print("This plate is not registered in the lot.")
        input("Please press enter to continue...")
        return     # Exits the function to go straight back to print_menu()   
    with open("vehicles.txt","w") as wf:    # Overwrites the text file and makes it completely blank
        wf.write("")
    for plate in plates:
        with open("vehicles.txt","a") as f:   # Appends text to the text file
            if plate not in open("vehicles.txt","r").read():   #  If the plate is not in the text file already, then it adds it otherwise it doesnt (to avoid repeating/duplicating plates)
                f.write(f"{plate}" "\n")
    print (f"{remove_plate} is removed")
    print(plates)
    input("Please press enter to continue...")
            
# Function to display charges and save everything to charges.txt file
def display_charges():
    check_password()
    print(f"Daily parking summary for 2023-10-29\n{'=' *60}\n{'Plate':>12}{'Credit Card':>23}{'Charge in $':>20}\n\n{'='*60}") # 
    x=0
    while x < len(plates): # While x is less then the index length of the list 'plates'
        print(f"{plates[x]:^20}{cc_numbers[x]:^20}{'4':^20}") # prints the index value of [x] (starting at 0 and increasing by 1 each time) for both plates and cc_numbers, and then prints charge of $4
        x+=1  # So that it goes through every item in the list and prints it
    
    y=0
    with open("charges.txt","w") as wf:
        wf.write("")
    while y < len(plates): # While y is less then the index length of the list 'plates'
        with open("charges.txt","a") as f:
            f.write(f"{plates[y]}{cc_numbers[y]:>12}{'4':>6}\n")
            y+=1 # So that it goes through every item in the list and prints it
    print(f"{'='*60}\n{'Total':^20}{x*4:^60}")
    input("Please press enter to continue...")
# Class and Function to clear all vehicles from the lot via admin privileges
class ParkingLot:
    def clear_vehicles(self):
        check_password()
        print("\nVehicles in the parking lot:")   # Displaying vehicles before clearing
        print(plates)
        plates.clear()   # Clears the vehicles / plates from the list 
        cc_numbers.clear() 
        with open("vehicles.txt","w") as wf:    # Overwrites the text file and makes it completely blank
            wf.write("")
        for plate in plates:
            with open("vehicles.txt","a") as f:   # Appends text to the text file
                if plate not in open("vehicles.txt","r").read():   #  If the plate is not in the text file already, then it adds it otherwise it doesnt (to avoid repeating/duplicating plates)
                    f.write(f"{plate}" "\n")
        print("All vehicles cleared from the parking lot!")
        print("\nVehicles after been cleared:")   # Displaying vehicles after clearing
        print(plates)
        input("Please press enter to continue...")


# Entire print menu function to display the menu and welcome message
def print_menu():
    option = int(input(f"{'*'*60}\n*** Welcome to Park and Go Parking Application! ***\nPark from 6 PM - Midnight for a flat fee of $4.00\n{'*'  * 60}\n" "Select from the following options\n1- Register a vehicle\n2- Verify vehicle registration\n3- Display registered vehicles and save them to a file\n4- Display daily charges and save them to a file\n5- Remove a vehicle\n6- Clear vehicles\n0- Exit\n>>> "))
    if option==0: # Exit option               ^^^ Displays menu and asks user to input a value between 0 and 6 for the different options the program provides
        print("Thanks and Good Bye!")
        exit()
    elif option==1:
         register_vehicle() # Register a vehicle
    elif option==2:
        verify_vehicle()   # Verify if a vehicle is registered or not
    elif option==3:
        pass # Display registered vehicles and save them to a file
    elif option==4:
        display_charges() # Display daily charges and save them to a file
    elif option==5:
        remove_vehicle()         # Remove a vehicle from the lot
    elif option==6:
        parking_lot = ParkingLot() # ParkingLot objects
        parking_lot.clear_vehicles()   # Calls on the function from earlier to clear all vehicles

    else:
        print("Invalid input, type a number between 0 and 6")
        input("Please press enter to continue...")

# A loop to continuously display the menu until the user explicitly decides to exit by inputting 0
while True:
    print_menu()      



