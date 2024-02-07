# list_comprehension_02.py
# Find all of the numbers from 1-1000 that have a 3 in them
numbers = list(range(1001))
num_with_3 = []

# for number in numbers:
#     if "3" in str(number):
#         num_with_3.append(number)

num_with_3 = [number for number in numbers if "3" in str(number)]
# or:
# num_with_3 = [number for number in range(1,1000) if "3" in str(number)]
print(num_with_3)