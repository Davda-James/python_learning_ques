import numpy as np
import math
# relating correlation (r) with cosine between vectors 
x=[1,2,5,6,8,9,15,11,10]
y=[4,3,12,13,7,9,14,1,2]
x=np.array(x)
y=np.array(y)
# mean of x and y
meanx=sum(x)/len(x)
meany=sum(y)/len(y)
# creating list X and Y
X=list(map(lambda alpha:alpha-meanx,x))
Y=list(map(lambda beta:beta-meany,y))
X=np.array(X)
Y=np.array(Y)
# r=(mean(xy)-mean(x)*mean(y))/(std(x)*std(y))
# finding standard deviation of x and y
stdx=(sum((x-meanx)**2)/len(x))**0.5
stdy=(sum((y-meany)**2)/len(y))**0.5
#finding x multiply y
xy=np.multiply(x,y)
# mean of xy
meanxy=sum(xy)/len(xy)
# finding XY
XY=np.multiply(X,Y)
# finding mode of X and Y
modXlist=list(map(lambda a:a**2,X))
modYlist=list(map(lambda b:b**2,Y))
modX=(sum(modXlist))**0.5
modY=(sum(modYlist))**0.5
# r (correlation coefficient)
r=format((meanxy-(meanx*meany))/(stdx*stdy),".14f")
# X.Y/|X||Y|
cosine=format(sum(XY)/(modX*modY),".14f")
print(f"the value of r is: {r} and the value of cosine is : {cosine}")
print("They both are equal and hence proved that r=cosine")
