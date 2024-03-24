data = [("name", "john"), ("age", 21)]
result = {k: v for k, v in data}
print(result)

result = {}
for i in range(1, 6):
    result[i] = i ** 2
print(result)


result = {i: i**2 for i in range(1, 6)}
print(result)

result = {i: i for i in range(1,5)}
print(result)

# zip() built-in function
keys = ["name", "age", "address"]
values = ["Jon", 30, "KTM"]

data = zip(keys, values)
print(dict(data))

# tuple comprehension
data = (i for i in range(5)) #it looks like tuple comprehension but it acutually is generator expression
print(data) #generator_expression

for i in data:
    print(i)










