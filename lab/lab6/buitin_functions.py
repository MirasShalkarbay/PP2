#1

# myList = [i for i in range(1,6)]

# result = 1

# for num in myList:
#     result *= num

# print(result)

# #2

# txt = input()

# count_lower = 0
# count_upper = 0

# for l in txt:
#     if l.isupper():
#         count_upper += 1
#     elif l.islower():
#         count_lower += 1

# print(f'Uppercase latters: {count_upper}')
# print(f'Lowercase latters: {count_lower}')

# # 3

# txt = input()

# if txt == txt [::-1]:
#     print('String is palindrome')
# else:
#     print('Srting is not palindrome')

#4

import math
import time

num =int(input())
milsec = int(input())

time.sleep(milsec / 1000)

print(f"Square root of {num} after {milsec} miliseconds is {math.sqrt(num)}")

#5

mytup1 = (True, True, False)
mytup2 = (True, True, True)

print(all(mytup1))
print(all(mytup2))