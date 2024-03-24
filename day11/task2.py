# check whether a number is palindrome number or not
#a = 121
#Output = “It is a palindrome number”
#A = 321
#output = “It is not a palindrome number”



num = int(input("enter a number "))
temp = num
summ = 0
while num != 0:
    r = num % 10
    summ = summ * 10 + r
    num = num // 10
if temp == summ:
    print("its is palindrome")
else:
    print("it is not palindrome")

num = input("enter a num ")
if num == num[::-1]:
    print("it is a palindrome number")
else:
    print("it is not a plaindrome number")



