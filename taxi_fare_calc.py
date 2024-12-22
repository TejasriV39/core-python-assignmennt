def calculate_fare(distance):
    base_fare = 50  
    distance_fare = 10 * distance  
    total_fare = base_fare + distance_fare  
    return total_fare

# User input
trips_input = input("Enter distances for trips separated by spaces (in km): ")
trips = trips_input.split()  # Splitting the input string into a list
trips = [float(distance) for distance in trips]  # Converting each distance to a float
# Initialize total fare
total_fare = 0  
for i in range(len(trips)):
    fare = calculate_fare(trips[i])  
    print("Trip {}: ${:.2f}".format(i + 1, fare))  
    total_fare += fare  # Add to total fare

print("Total Fare: ${:.2f}".format(total_fare))