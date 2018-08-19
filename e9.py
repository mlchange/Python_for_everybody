name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    
    if not line.startswith('From '):continue
    words=line.split()
    counts[words[1]]=counts.get(words[1],0)+1

Bigcount=None
Bigword=None
for word,count in counts.items():
    if Bigcount is None or count>Bigcount:
        Bigcount=count
        Bigword=word
print(Bigword,Bigcount)