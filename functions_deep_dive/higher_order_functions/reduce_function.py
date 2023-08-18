letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:

# remember to import the reduce function
from functools import reduce
# store the result of your reduce function in the variable word
word = reduce(lambda str1, str2: str1 + str2, letters)

# print word
print(word)