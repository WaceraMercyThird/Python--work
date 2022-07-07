#Variables and Names

cars = 100.0  # cars are 100
space_in_a_car = 4 # the capacity of the car is 4.
drivers = 30 # drivers are 30 in number.
passengers = 90 # passengers are 90 people
cars_not_driven = cars - drivers # so cars that were not driven is all of those cars subtracting drivers that were not available to drive the remaining cars. 
cars_driven = drivers # cars that were driven is for those that drivers were available to drive them.
carpool_capacity = cars_driven * space_in_a_car # To find out the capacity for the driven cars you multiply the number by the space in a car.
average_passengers_per_car = passengers / cars_driven #the avarage passengers per car will be dividing the number of passengers with cars that were driven.

# average_passengers_per_car = car_pool_capacity / passengers # In line 8 there is unexpect underscore between car and pool which is not being recognized by the interpretor.
 
 
print("There are", cars, "cars available.") 
print("There are only", drivers, "drivers available.") 
print("There will be", cars_not_driven, "empty cars today.") 
print("We can transport", carpool_capacity, "people today.") # when space_in_a_car is 4 instead of 4.0 the output will whole number not a float poin number when we multiply by cars_driven.
print("We have", passengers, "to carpool today.") 
print("We need to put about", average_passengers_per_car,"in each car.") 