# what are methods?
# those functions that are defined inside a class are called methods

# functions
# 1 built-in functions
# 2 user-defined functions
# 3 built-in methods (those functions that are already defined in python classes)
# 4 user-defined methods (those functions that are defined inside user-defined class)

 # list methods
# append()
from copy import deepcopy


a = [1, 2, 3]
a.append(4)
print(a)

#extend()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# insert()
vowels = ["a", "e", "i", "o","u"]
vowels.insert(2, "t")
print(vowels) #["a", "e", "t", "i", "o","u"]

# index()
vowels = ["a", "e", "i", "o","u"]
result = vowels.index("i")
print(result) #2

#remove()
vowels = ["a", "e", "i", "o","u"]
vowels.remove("o")
print(vowels) #["a", "e", "i", "u"]

# pop()
vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop()
print(vowels)  # ["a", "e", "i", "o"]
print(result)  # "u"

vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop(3)
print(result)  # "o"
print(vowels)  # ["a", "e", "i", "u"]

# vowels.pop(10)  # It raises error.


# count()
data = [3, 2, 1, 1, 1, 3, 3, 3, 3, 4, 5]
result = data.count(1)
print(result)  # 3

# print(data.count())  # It raises error


# clear()
vowels = ["a", "e", "i", "o", "u"]
vowels.clear()
print(vowels)  # []


# copy()
a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True

b = a.copy()
print(a == b)  # True
print(a is b)  # False


# Concept of shallow copy and deep copy
a = [1, 2, [3, 4]]
b = a.copy()

a[2][1] = 7
print(a)  # [1, 2, [3, 7]]
print(b)  # [1, 2, [3, 7]]


# from copy import deepcopy
b = deepcopy(a)

a[2][1] = 9
print(a)  # [1, 2, [3, 9]]
print(b)  # [1, 2, [3, 7]]