#for assignment 3

# calculates area with 2 inputs
def house_sqft():
    # gives users one extra try if they don't type numbers
    try:
        #convert to float so they can use decimal numbers
        length = float(input("What is the length in feet of your house? "))
        width = float(input("What is the width in feet of your house? "))
    except: 
        # clear error message and then let them retry once.  
        print('Numbers needed for "length" and "width".')
        length = float(input("What is the length in feet of your house? "))
        width = float(input("What is the width in feet of your house? "))
    #basic formula
    area = length * width
    #show the result
    print("Your house is " + str(area) + " square feet.")
    #return as a float if they want to do additional math
    return(area)

#Circumference calculator with input for radius and unit
def circle_circum():
    # improted pi for exact answers
    from math import pi
    # gives users one extra try if they don't type numbers
    try:
        #used float so they can use exact numbers
        radius = float(input("What is the radius of your circle? "))
    except: 
        # clear error message and then let them retry once.
        print("please type numbers for circumference")
        radius = float(input("What is the radius of your circle? "))
    #not necessary, but makes it look nice
    unit = input("What unit is the radius in ")
    #basic formula
    circumference = 2 * pi * float(radius)
    #friendly print message
    print("Your circle is " + str(circumference) + " " + unit)
    #return used in case further math is wanted
    return(circumference)

house_sqft()
circle_circum()
