#WAP to delete all the occurrences of a specified character in a given string 
#S = “All the occurrences of a specified character in a given string”
#Input = “a”
#Output = “ll occurrences of  specified chrcter in  given string”


s = "all the occurrences of a specified character in a given string"
char = input("enter the character you want to remove ")
result = ""
for each in s:
    if each.lower() == char.lower():
        continue
    result += each 
print(result)

