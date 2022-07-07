# Printing, Printing

formatter = "{} {} {} {} {} {} {} {}" 

print(formatter.format(1, 2, 3, 4,5, 6, 7, 8)) 
print(formatter.format("one", "two", "three", "four","one", "two", "three", "four")) 
print(formatter.format(True, False, False, True, True, False, False, True)) 
print(formatter.format(formatter, formatter, formatter, formatter, formatter, formatter, formatter, formatter))
print(formatter.format( 
    "Try your", 
    "Own text here", 
    "Maybe a poem", 
    "Or a song about fear",
    "Try your", 
    "Own text here", 
    "Maybe a poem", 
    "Or a song about fear"  
 )) 
