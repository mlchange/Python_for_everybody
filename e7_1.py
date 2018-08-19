# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count=0
confident=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count=count+1
    n=line.find(':')
    confident=confident+float(line[n+1:])

print("Average spam confidence:",confident/count)