
fh = open('romeo.txt')
lst = list()
for line in fh:
    a=line.split()
    for b in a:
        if b in lst:
            continue
        lst.append(b)
lst.sort()
print(lst)