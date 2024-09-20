"""Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out the total, count and average of the numbers.
If the user enters anything other than the number, detect their mistake using try and except and
print an error message and skip to the next number."""

count = 0
total = 0.0
while True :
    value = input("Enter number: ")    #entered this line before while and got error
    if value == 'done':
        break
    try :
       floatvalue = float(value) 
    except :
        print( "Invalid Input.Try Again.")
        continue
    count = count + 1
    total = total + floatvalue

print("Total:",total,"Count:", count ,"Average", total/count ) #forgot coma(,) after "Total"