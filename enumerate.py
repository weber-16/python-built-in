'''return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on.'''
# Accessing items using enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for i, x in enumerate(cars):
    print (x)
# we can also write in 
# Accessing items and indexes enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars):
    print (x[0], x[1])
# also in

# demonstrating the use of start in enumerate

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
    print (x[0], x[1])
