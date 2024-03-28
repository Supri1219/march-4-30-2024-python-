#lambda is the anonymous function in python 

data = [1, 2, 3, 4, 5]


result = map(lambda x: x + 10, data)

print(list(result))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = filter(lambda x: x % 2 != 0, data)

print(list(result))  

from functools import reduce
data = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x +y, data)
print (result)

