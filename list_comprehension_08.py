# list_comprehension_08.py
# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
numbers = range(20)
even_odd = []

# for number in numbers:
#     if number % 2 == 0:
#         even_odd.append("even")
#     else:
#         even_odd.append("odd")

# or
even_odd = ["even" if number % 2 == 0 else "odd" for number in numbers]

print(even_odd)