# List is the mutuable data type in python
# they are the sequence of data enclosed within big brackets
# unlike array, the elements in list can be heterogeneous datatype 
# creating an empty list
a = list() # empty list []
print (a)
a=[]

a= [1, 2, 3]
print (a)
b = ["hello", "world"]
print (b)
c = [1, 2, "hello", [4,5]]

# accessing the list elements
# list elements can be accessed using indexing and slicing

# indexing
# forward indexing
vowels = ["a", "e", "i", "o", "u"]
print (vowels[3])
print (vowels[0])

# negative indexing
print (vowels[-1])
print (vowels[4] == vowels[-1])

# slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(data[2:7])  # ["c", "d", "e", "f", "g"]
print(data[:4])  # ["a", "b", "c", "d"]
print(data[0:4])  # ["a", "b", "c", "d"]
print(data[5:])  # ["f", "g", "h", "i", "j"]
print(data[1:9:2])  # ["b", "d", "f", "h"]
print(data[9:1])  # []

print(data[-8:-2])  # ["c", "d", "e", "f", "g", "h"]
print(data[:-3])  # ["a", "b", "c", "d", "e", "f", "g"]
print(data[-4:])  # ["g", "h", "i", "j"]
print(data[-3: -9])  # []

data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(data[2:8]) # ["c", "d", "e", "f", "g", "h"]
print(data[9:3]) # []
print(data[7:]) # ["h", "i", "j"]
print(data[:4]) # ["a", "b", "c", "d"]
print(data[-5:-9]) # []
print(data[-4: -8]) # []
print(data[3:-1]) # ["d", "e", "f", "g", "h", "i]
