# list_comprehension_06.py
# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4] 
list_b = [2, 3, 4, 5]
result = []


# for item_a in list_a:
#     for item_b in list_b:
#         if item_a == item_b:
#             result.append(item_a)

# or
# result = [item_a for item_a in list_a for item_b in list_b if item_a == item_b]

# or
# for item_a in list_a:
#     if item_a in list_b:
#         result.append(item_a)

# or
result = [item_a for item_a in list_a if item_a in list_b]

print(result)