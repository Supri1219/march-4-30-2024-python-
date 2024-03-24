#WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and  1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.

hour = float(input("enter the hour"))
rate = float(input("enter rate per hour"))
if hour > 40:
    gross_pay = (40*rate) + ((hour-40)*rate*1.5)
    print(f"total gross pay is {gross_pay}")
else:
    gross_pay = hour * rate
    print (f"total gross pay is {gross_pay}")

    
