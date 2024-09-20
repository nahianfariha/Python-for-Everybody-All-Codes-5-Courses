""" Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other
than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below."""


largest = None
smallest = None 
while True :
    number = input("Enter any number:") 
    if number == 'done':
        break
    try :
        num = float(number)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num 
    except :
        print("Invalid input")
        continue
    
if smallest is not None and largest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("Invalid input")


    """If you don't include the continue statement in the except block, the program will still function correctly in this specific case.
    The continue statement is used to skip the rest of the current loop iteration and move to the next iteration. However, since the 
    print("Invalid Input. Next?") is the last line in the except block, the loop will naturally continue to the next iteration
    after printing the error message."""