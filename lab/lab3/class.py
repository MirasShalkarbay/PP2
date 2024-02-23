#Ex 1
class Stringinput:
    def __init__(self):
        self.input = ""
    def get_string(self):
        self.input = input("")
    def printString(self):
        print(self.input.upper())

string_input = Stringinput()
string_input.get_string()
string_input.printString()

#Ex 2
class Shape:
    def __init__(self):
        self.area = 0

    def defolt(self):
        print("defolt area of the shape {}".format(self.area))

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def calculate_area(self):
        self.calculate_area = self.length ** 2
        print(self.calculate_area)

length_input = float(input())
square = Square(length_input)
square.calculate_area()
square.defolt()

#Ex 3
class Shape:
    def __init__(self):
        self.area = 0

    def defolt(self):
        print("defolt area of the shape {}".format(self.area))

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def area_of_rectangle(self):
        print(self.area)

l = int(input())
w = int(input())

rectangle = Rectangle(l, w)
rectangle.area_of_rectangle()

#Ex 4
import random
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x)
        print(self.y)
    
    def move(self):
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        print(self.x , self.y)

    def dist(self, other):
        return(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))

dx1 = int(input())
dy1 = int(input())

crd = Point(dx1, dy1)
crd.show()
crd.move()

dx2 = int(input())
dy2 = int(input())
crd2 = Point(dx2, dy2)

distance = crd.dist(crd2)
print(distance)

#Ex 5
class Bank():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. New balance: {self.balance}")
        else:
            print('incorrect amount')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} has been withdrawn. New balance: {self.balance}")
        elif(amount > self.balance):
            print("Withdrawal amount exceeds available balance.")
        else:
            print("incorrect amount")


person = Bank("Miras Shalkarbay", 1000)

person.deposit(500)
person.withdraw(900)
person.withdraw(200)
person.deposit(-100)

#Ex 6
class Filter():
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))
    
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_filter = Filter(numbers_list)

filtered_primes = prime_filter.filter_primes()
print(filtered_primes)
