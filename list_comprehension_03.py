# list_comprehension_03.py
# Count the number of spaces in a string

s = "Count the number of spaces in a string"
spaces = []

# for letter in s:
#     if letter == " ":
#         spaces = spaces + 1

# or
spaces = [letter for letter in s if letter == " "]

print(len(spaces))

# or
print(s.count(" "))