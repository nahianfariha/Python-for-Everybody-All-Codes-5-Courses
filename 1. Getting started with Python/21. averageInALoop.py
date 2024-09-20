count = 0
sum = 0
print("Before", count)
for num in[5,8,0,33,24,90]:
    count = count + 1
    sum = sum + num
    print(count, num)
print("Count",count,"sum", sum)
print("Average", sum/count)