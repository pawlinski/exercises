# list_comprehension_07.py
# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’

sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
numbers = []

# for letter in sentence:
#     if letter.isnumeric():
#         numbers.append(letter)

# or
numbers = [letter for letter in sentence if letter.isnumeric()]

print(numbers)