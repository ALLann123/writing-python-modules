#!/usr/bin/python3
from rectangle import calc_area, calc_perimeter

print("Lets calculate area and perimeter")
#get inputs
length=int(input("Enter the length>> "))
width=int(input("Enter the width>> "))

#calculate the area and perimeter using the libraries
area=calc_area(length,width)
perimeter=calc_perimeter(length,width)

#display output
print(f"The area is {area}")
print(f"The perimeter is {perimeter}")
