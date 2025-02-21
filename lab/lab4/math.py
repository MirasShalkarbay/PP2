#Ex 1
import math

degree = float(input())

radian = degree * (math.pi / 180)
print(radian)

#Ex 2
import math 

hight = int(input("Hight: "))

Base = int(input("Base, first value: "))
Base2 = int(input("Base, second value: "))

area = 1/2*(Base + Base2)*hight

print(area)

#Ex 3
import math 

sides = int(input("Input number of sides: "))
lenght = int(input("Input the lenght of sides: "))

area = sides * (lenght**2)* (math.tan(math.pi/sides)/4)

print(area)

#Ex 4
import math 

a= int(input())
b = int(input())

area = a * b

print(float(area))