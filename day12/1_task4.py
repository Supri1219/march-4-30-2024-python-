students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]
import functools
def sum_of_age(x, y):
    if type(x) == dict:
        return x['age'] + y['age']
    return x + y["age"]
result = functools.reduce(sum_of_age, students)
print(result)
