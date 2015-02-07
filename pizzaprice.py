# pizzaprice
calculate the price per square inch of a pizza

import math
def main():
    
    diameter = eval(input("What is the diameter of the pizza? "))
    price = eval(input("What is the price of the pizza? "))

    area = math.pi * (diameter / 2) ** 2
    cost = price / area

    print("The cost per square inch of this pizza is", cost)

main()
                  
