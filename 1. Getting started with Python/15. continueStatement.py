while True :
    line = input('')
    if line[0] == '#' :    #here line[0] indicates first character of the line.
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
        