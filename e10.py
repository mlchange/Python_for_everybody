name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times=dict()
for line in handle:
    
    if not line.startswith('From '):continue
    words=line.split()
    time=words[5].split(':')
    times[time[0]]=times.get(time[0],0)+1

a=list()
for key,value in times.items():
    a.append((key,value))

a=sorted(a)
for key,value in a:
    print(key,value)
