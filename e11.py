import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_39849.txt"
handle = open(name)
su=0
count=0
for line in handle:
    stuff=re.findall('[0-9]+',line)
   
    for num in stuff:
        su=int(num)+su
        count=count+1
    
print('sum of number is',su,'count is',count)


print( sum( [ ****** *** * in **********('[0-9]+',**************************.read('regex_sum_39849.txt')) ] ) )