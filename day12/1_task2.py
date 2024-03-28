students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]

def greater_than_twentyfive(element):
    if element['age'] > 25:
        return True  
    return False 


result = filter(greater_than_twentyfive, students)

print(list(result))