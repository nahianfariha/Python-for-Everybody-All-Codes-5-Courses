#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.

hours = input("Enter Hours:")
h = float(hours)
rateperhour = input("Enter rate per hour:")
r = float(rateperhour)
if h > 40 :
    regular_pay = 40*r
    overtime_pay = (h - 40) * (1.5 * r)
    gross_pay = regular_pay + overtime_pay

else :
    gross_pay = h*r

print(gross_pay)