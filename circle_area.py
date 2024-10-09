import math   # import math to be able to use pi formular

def circle_area(radius):            #define circle_area function with parameter radius
    area = math.pi * radius**2      # usage of formular A = π * r^2 with math.pi ^=**
    return area                     # set variabel area and return area
radius = 3                          # you can change the value of radius
result = circle_area(radius)        # set variable for the result
print(f"The area of the circle with the radius {radius} is: {result:.2f}")
# usage of f-String to output the result within a nice sentence.