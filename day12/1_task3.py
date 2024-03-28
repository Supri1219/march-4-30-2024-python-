students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]

def uppercase(element):
    element['name'] = element['name'].upper()
    return element
result = map(uppercase, students)
print(list(result))