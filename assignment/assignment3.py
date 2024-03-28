#3
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'c': 400}
print("d1", str(d1))
print("d2", str(d2))
final_dictionary = {x: d1.get(x, 0) + d2.get(x, 0)
                    for x in set(d2).union(d1)}
print("final dictionary", str(final_dictionary))



