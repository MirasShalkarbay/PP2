 #Ex 1
def square(N):
    for i in range(1, N+1):
        yield i**2

N = int(input())

for square1 in square(N):
    print(square1)

#Ex 2
def even(n):
    for i in range(0, n):
        if(i % 2 == 0):
            yield i

n = int(input())

for even1 in even(n):
    print(even1)

#Ex 3
def t_and_f(n):
    for i in range(0, n):
        if(i % 3 == 0 and i % 4 == 0):
            yield i

n = int(input())
for numbers in t_and_f(n):
    print(numbers)

#Ex 4
def square(a,b):
    for i in range(a,b+1):
        yield i**2

a = int(input())
b = int(input())

for answer in square(a,b):
    print(answer)

#Ex 5
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for number in countdown_generator(n):
    print(number)