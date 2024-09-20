# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fr = fh.read()
count = 0
for line in fr:
    if line.startswith("X-DSPAM-Confidence:"):
        
        fm = fr.find(':')
        fn = fm[fm+1 : ]
        ff = float(fn)
        continue
        count = count+1
        avg = ff/count
    print('Average spam confidence:', line)

