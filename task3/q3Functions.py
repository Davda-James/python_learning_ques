#a. printing 1 if leap year and 0 if not 
year=int(input("enter year: "))
if year%4==0 and year%100!=0:
    print("entered year is leap year")
elif year%100==0 and year%400==0:
    print("year entered is leap year")
else:
    print("entered year is NOT leap")

#b. checking whether triangle is equilateral,isoceles,scalene
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if a+b<=c or b+c<=a or a+c<=b:
    print("sorry wrong sides of triangle")
elif a==b==c :
    print("triangle is equilateral")
elif a!=b and b!=c and a!=c:
    print("triangle is scalene")
else:
    print("triangle is isoceles")

