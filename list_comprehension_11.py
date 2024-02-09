# list_comprehension_11.py
# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
numbers = range(1, 1001)
div = range(2, 10)
result = []

# for number in numbers:
#     for d in div:
#         if number % d == 0:
#            result.append(number)
#            break

# or

# for number in numbers:
#     if any(number % d == 0 for d in div):
#         result.append(number)


# or

result = [number for number in numbers if any(number % d == 0 for d in div)]


print(result) 