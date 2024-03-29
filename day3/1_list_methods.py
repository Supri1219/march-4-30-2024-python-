# March 10

# sort() and reverse()


a = [5, 1, 3, 10, 12, 4]
a.sort()  # ascending order sort
print(a)

a = ["banana", "apple", "orange"]
a.sort()
print(a)
print(a.sort()) #none 

a.sort(reverse=True)  # descending order sort
print(a) #wont return


# reverse()
a = [5, 1, 3, 10, 12, 4]
a.reverse()
print(a)  # [4, 12, 10, 3, 1, 5]