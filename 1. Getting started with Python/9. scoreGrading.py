"""Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85."""

"""
how i did at first:
score = input("Enter Score: ")
x = float(score)

if x < 0.6 :
    print("F")
elif x >= 0.9 :
    print("A")
elif x >= 0.8 :
    print("B")
elif x >= 0.7 :
    print("C")
elif x >= 0.6 :
    print("D")
else :
    print("Out of Range")"""

def compute_grade(score):
    if score < 0.0 or score > 1.0:
        return "Error: Score is out of range."
    elif score >= 0.9 and score <= 1.0:
        return "A"
    elif score >= 0.8 and score < 0.9:
        return "B"
    elif score >= 0.7 and score < 0.8:
        return "C"
    elif score >= 0.6 and score < 0.7:
        return "D"
    else:
        return "F"


score = float(input("Enter a score between 0.0 and 1.0: "))
grade = compute_grade(score)
print("Grade:", grade)


#there were some logic errors.again, while i was revising i fixed the errors. I am proud of me. :)