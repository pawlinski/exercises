# list_comprehension.py
# Find all of the numbers from 1-1000 that are divisible by 7

numbers = list(range(1001))
# print(numbers[-1])  # print last element from list

numbers_div_7 = []

# for number in numbers:
#     if number % 7 == 0:
#         numbers_div_7.append(number)

# print(numbers_div_7)

# list comprehension:
numbers_div_7 = [number for number in numbers if number % 7 == 0]
# or
# numbers_div_7 = [number for number in range(1,1000) if number % 7 == 0]

print(numbers_div_7)