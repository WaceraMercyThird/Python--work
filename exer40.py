# Modules, Classes, and Objects


from sys  import mystuff

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])


mystuff.apple()
# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"



mystuff.apple()
print(mystuff.tangerine)


mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable