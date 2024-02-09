# list_comprehension_10.py
# Find all of the words in a string that are less than 4 letters
sentence = "Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made)."
result = []

# for word in sentence.split(" "):
#     if len(word) < 4:
#         result.append(word)

# or 
result = [word for word in sentence.split(" ") if len(word) < 4]

print(result)