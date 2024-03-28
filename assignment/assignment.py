#1 python + is + an + awesome + language 
data = "python + is + an + awesome + language"
a = list(data)
print(a)
char = input("enter the character you want to remove ")
result = ""
for each in data:
    if each == char:
        continue
    result += each
print (result)







