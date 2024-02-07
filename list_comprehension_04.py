# list_comprehension_04.py
# Create a list of all the consonants(spółgłosek) in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”

s = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = []
vowels = ["a", "e", "i", "o", "u", "y", " "]

# for letter in s:
#     if letter.lower() not in vowels:
#         consonants.append(letter)

# or
consonants = [letter for letter in s if letter.lower() not in vowels]

print(consonants)
print(len(consonants))