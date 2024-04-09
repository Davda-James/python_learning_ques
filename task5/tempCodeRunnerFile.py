x,k=input().split(" ")
x=int(x)
k=int(k)
p=input()
s=p.split(" + ")
power=[]
for i in range(len(s)-2):
    a=s[i].split("**")[1]
    power.append(int(a))
power=power+[1,0]
sum=0
for j in range(len(power)):
    if power[j]==0:
        sum=sum+1
    else:
        sum=x**power[j]+sum
if sum==k:
    print("True")
else:
    print("False")