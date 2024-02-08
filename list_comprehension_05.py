# list_comprehension_05.py
# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
some_list = ["hi", 4, 8.99, 'apple', ('t,b','n')]
new_list = []

# for index, value in enumerate(some_list):
#     new_list.append((index, value))

# or
new_list = [(index, value) for index, value in enumerate(some_list)]

print(new_list)