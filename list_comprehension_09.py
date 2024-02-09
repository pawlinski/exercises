# list_comprehension_09.py
# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
result = []

# for number in list_a:
#     if number in list_b:
#         result.append(tuple((number, number)))

# or
result = [tuple((number, number)) for number in list_a if number in list_b]

print(result)