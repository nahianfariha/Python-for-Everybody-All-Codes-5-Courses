def func(x) :
    print(x)
func(10)
func(20)

"""What does the following Python code print out? (Note that this is a bit of a trick question and the code 
has what many would consider to be a flaw/bug - so read carefully).
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
ChatGPT
This Python code defines a function addtwo(a, b) that adds two numbers a and b, assigns the result 
to a variable added, but then returns only the value of a. Then, it calls this function with arguments 2 and 7,
 and assigns the returned value to variable x. Finally, it prints the value of x.

The code will print 2.

The function addtwo(a, b) correctly adds a and b, but it always returns the value of a, 
regardless of the value of added. So, when you call addtwo(2, 7), it returns 2, and x is assigned this value. 
Therefore, when you print x, it prints 2."""