# Tuples are immutable datatypes in Python
# They are sequence of heterogeneous data types enclosed within small brackets (iterable)

# int
# float
# list
# tuple
# dict
# set
# bool
# complex

# Creating empty tuples
a = ()
print(a)
b = tuple()


# Creating non-empty tuples
a = [1, 2, 3]
b = tuple(a)  # type casting
print(b)  # tuple datatype

c = ("a", "e", "i", "o", "u")

# Accessing tuple elements
# Tuple elements can also be accessed using indexing and slicing similar to list

# Indexing
# Forward indexing starts from 0 while reverse indexing from -1
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # "a"
print(vowels[3])  # "o"
print(vowels[-1])  # u
# print(vowels[10])  # IndexError
# print(vowels[-10])  # IndexError

# Slicing
# Slicing is also similar to the list slicing

