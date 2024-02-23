#Ex 1
def ounces_to_grams(grams):
    print(28.3495231 * grams, 'ounces')
grams = int(input())
ounces_to_grams(grams) 

#Ex 2
def F_to_C(F):
    print('C = ', (5 / 9) * (F - 32) )
F = int(input())
F_to_C(F)

#Ex 3
def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if 4*r + 2*c == numlegs:
            return c, r
numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))

#Ex 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(list):
    result = []
    for num in list:
        if is_prime(num):
            result.append(num)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_prime(numbers)

print(result)
    
#Ex 6
def rev(string):
    list = string.split()
    list.reverse()
    for i in list:
        print(i, end = ' ')
s = input()
rev(s)

#Ex 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            print('True')
            break
    else:
        print('False')
    pass

list = []
n = 1

while n != 0:
    n = int(input())
    if n != 0:
        list.append(n)
has_33(list)

#Ex 8
def spy_game(array):
    for i in range(len(array) - 2):
        if array[i] == array[i + 1] == 0 and array[i + 2] == 7:
            return True
    return False

numbers = [1,0,2,4,0,0,7]
result = spy_game(numbers)
print(result)

#Ex 9
from math import pi

def volume_of_sphere(radius):
    vol = float(4/3 * pi * pow(radius,3))
    return vol

r = float(input())
print(volume_of_sphere(r))

#Ex 10
def unique(input_list):
    unique_list = []
    for elements in input_list:
        if elements not in unique_list:
            unique_list.append(elements)
    return unique_list

list = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 6, 1, 10]
print(unique(list))

#Ex 11
def is_palindrome(word):
    if word == word[::-1]:
        return ('is palindrome')
    else:
        return ('is not palindrome')

Word = str(input())
print(is_palindrome(Word))

#Ex 12 
def histogram(list):
    result = "" 
    for i in list:
        result += '*' * i + '\n'
    return result
array = [int(x) for x in input().split()]
print(histogram(array))

