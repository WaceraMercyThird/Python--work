# String and text

types_of_people = 10 # a valiable that contains the number of how many types of people there is
x = f"There are {types_of_people} types of people." # formating a string using f-sting method............
 
binary = "binary" # valiable called binary contains binary string.............
do_not = "don't" # valiable called do_not contains don't string...........
y = f"Those who know {binary} and those who {do_not}." 

# printing both x and y valiable
print(x) 
print(y) 
#printing both x and y through using f-string formatting to contract it in another string..........
print(f"I said: {x}") 
print(f"I also said: '{y}'") 

# Two valible hilarious and joke evaluation containing False and a string"Isn't that joke so funny?!" respeatively. 
hilarious = False 
joke_evaluation = "Isn't that joke so funny?! {}" 

 #S.format method to print out two valiables.
print(joke_evaluation.format(hilarious)) 
  
# We have two valiable w and e with strings then invoke the two by concatenating the valiables.
w = "This is the left side of..." 
e = "a string with a right side." 
 
print(w + e) # w and e with + make a longer string because they are valiable containing stings.



