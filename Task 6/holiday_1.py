city_flight = (input("would you like to travel to amsterdam, bruge or cairo ? "))
num_nights = int(input("How many nights are you traveling for? "))
rental_days = int(input("How many days do you need a car for? "))

#print(f"To confirm that is destination {city_flight} for a total of {num_nights} days and {rental_days} days car hire.")

def hotel_cost(num_nights):
    # fixed cost per night
    cost_per_night = 100 
    
    # Calculate the total hotel cost
    total_cost = num_nights * cost_per_night
    
    # Return the total hotel cost
    return total_cost

#print(f"The total hotel cost for {num_nights} nights is: GBP{hotel_cost(num_nights)}")


#print("Now for your flight costs...one sec, just calculating")

def plane_cost(city_flight):
    # flight costs for each destination
    cost_destination_a = 299  
    cost_destination_b = 395  
    cost_destination_c = 420  
    
    # Determine the flight cost based on the city_flight
    if city_flight == 'amsterdam':
        return cost_destination_a
    elif city_flight == 'bruge':
        return cost_destination_b
    elif city_flight == 'cairo':
        return cost_destination_c
    else:
        return "Invalid destination"

#print(f"The flight cost for destination {city_flight} is: GBP{plane_cost(city_flight)}")

#print("Now for your car rental...one sec, just calculating")

def car_rental(rental_days):
    # fixed cost per day
    cost_per_day = 70  
    
    # Calculate the total car hire
    total_car_cost = rental_days * cost_per_day
    
    # Return the total hotel cost
    return total_car_cost

#print(f"The total car rental for {rental_days} days is: $ {car_rental(rental_days)} ")

def holiday_cost(num_nights, city_flight, rental_days):

    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_cost = car_rental(rental_days)

    final_cost = total_hotel_cost + total_plane_cost + total_car_cost
    return final_cost

total_final_cost = holiday_cost(num_nights, city_flight, rental_days)

print(f"I'm excited to confirm you have chosen the magical {city_flight} for your dream holiday! You'll staying for {num_nights} nights and with {rental_days} car hire. ")
print(f"The total cost for this trip of a lifetime is GBP {holiday_cost(num_nights, city_flight, rental_days)}")
