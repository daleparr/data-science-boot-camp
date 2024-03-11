sum_of_numbers = 0
count = 0

while True:

    user_input =input ("Enter any number, or -1 to stop: ")
    number = int(user_input)

    if number == -1:
        break
    sum_of_numbers +=number
    count +=1

if count > 0:
    average = sum_of_numbers / count
    print(f"The average of the numbers entered is: {average}")

else:
    print("No numbers were input.")

