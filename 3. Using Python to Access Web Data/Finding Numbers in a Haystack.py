import re
inputfile = input("Enter file name:")
total = 0
fileopening = open(inputfile) 
filereading = fileopening.read()
numbercount = re.findall('[0-9]+',filereading)
total = sum(int(num) for num in numbercount)

print(total)