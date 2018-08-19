hrs = input("Enter Hours:")
rate=input("Enter rate:")
try:
    h = float(hrs)
    r=float(rate)
except:
    print("error")
    quit()
if h<=40:
    print(r*h)
else:
    print(r*40+1.5*r*(h-40))
