# student_register.py

def register_students():
    # Ask the user how many students are registering
    num_students = int(input("How many students are registering? "))

    # Open a text file for writing the student IDs
    with open("reg_form.txt", "w") as file:
        # Loop through the number of students to register
        for _ in range(num_students):
            # Ask the user for the next student ID number
            student_id = input("Enter the next student ID number: ")
            # Write the student ID and a dotted line for the signature to the file
            file.write(f"{student_id}\n")
            file.write("............................\n")

    print("Registration complete. Student IDs have been saved to reg_form.txt.")

# Call the function to start the registration process
if __name__ == "__main__":
    register_students()
