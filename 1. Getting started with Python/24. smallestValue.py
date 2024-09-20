"""In Python, None is a special constant representing the absence of a value or a null value. 
It is an object of its own datatype, the NoneType, and it is often used to signify that a variable 
does not have a value assigned to it or that a function does not return a value."""

smallest = None
print("Comparing")
for value in [22,11,89,2,9]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("Smallest", smallest)

#"is" is used mostly in True, False and None