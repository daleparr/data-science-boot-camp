city_flight = (input("would you like to travel to a, b or c ?"))
a = 669
b = 419
c = 129
num_nights = int(input("How many nights are you traveling for? "))
rental_days = int(input("How many days do you need a car for? "))

print(f"To confirm that is destination {city_flight} for a total of {num_nights} days and {rental_days} days car hire.")
print("Now let me work out your accommodation costs...one second")
hotel_cost = num_nights * 459

print(f"The total cost of the accomdation will be GBP{hotel_cost}" )
print("Now let me work out your car hire costs...one second")

rental_cost = rental_days * 129
print(f"The total cost of the accomdation will be GBP{rental_cost}" )

print(f"Your total cost is ")