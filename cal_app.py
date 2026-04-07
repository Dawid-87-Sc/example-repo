# write a perform calculation under one def:
def perform_calculations():
    while True: # use while true for if function is true
        try:# use try for failsave and math equation
            #user enter number through app
            num_1=float(input("Enter a first number:"))
            num_2=float(input("Enter a second number:"))
            operation= input("Enter the operation you want to use (+,-,*,/):")
# operations that must be done for point 3:
            if operation== "+":
                result= num_1 + num_2
                print(result)
                
            elif operation== "-":
                result= num_1 - num_2
                print(result)
                
            elif operation== "*":
                result = num_1 * num_2
                print(result)
                
            elif operation== "/":
                result = num_1 / num_2
                print(result)
            else:
                print("Incorrect numbers were enter, try again")
                return

            with open('equation.txt','a+', encoding= 'utf-8') as file:
                file.write(f"{num_1} {operation} {num_2} = {round(result, 2)}\n")
                print("\nYour results have been successfully stored in equations.txt")
          

        except Exception:
            print("That was not a value entry, try again")
            return(perform_calculations)
        perform_calculations()
        print(perform_calculations)

# Start app questions for chosing
def print_previous_equations():
    """
    Reads and displays previous equations from equations.txt. Handles file errors.
    """
    try:
        with open('equations.txt', 'r', encoding='utf-8') as file:
            equations = file.readlines()
        # Print equations if there is something in the file. 
        if equations:
            print("\nPrevious equations:")
            for equation in equations:
                print(equation.strip())
        else:
            print("\nNo previous equations found.")
    except FileNotFoundError:
        print("No previous equations found.")

                
def calc_app():
    """
    Presents the calculator menu, handles user choices, and exits when necessary.
    """
    while True:
        print("\nWelcome to the Calculator App!")
        print("1. Perform Calculation")
        print("2. Print Previous Equations")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        # Call functions based on user choice.
        if choice == '1':
            perform_calculations()
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            break  # Exit the loop, ending the program
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# Start the app
calc_app()


