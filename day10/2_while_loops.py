# While loop is used with conditions or Truthy or Falsy values
# We should always update the condition variable from inside the while block.
# If the condition variable is not updated then the loop goes to infinite

a = 0
while a <= 10:
    print(a)
    a += 1


#Create a new list of repeated items from a provided list:
nums = [3, 4, 2, 2, 1, 3, 3, 3]
Output = [3, 2]

nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for each in nums:
    if nums.count(each) > 1 and each not in result:
        result.append(each) 
        print(result)

#WAP to print a list of first 10 natural numbers using a for loop
result = list()    
for i in range(1, 11):
    result.append(i)
    print(result)

#list comprehension
result = [i for i in range(1, 11)]
print(result)

# [2, 4, 6, 8, 10]

result = list()
for i in range(2, 11, 2):
    result.append(i)
    print(result)

even = []
for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)

print(even)   # [2, 4, 6, 8, 10]

result = [i for i in range(1, 11) if i % 2 == 0]  # comprehension with condition
print(result)

# Create [1, 4, 9, 16, 25] using list comprehension
result = [i**2 for i in range(1, 6)]
print(result)




