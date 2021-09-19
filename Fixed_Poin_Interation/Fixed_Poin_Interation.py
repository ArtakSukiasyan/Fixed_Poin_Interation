def F(x):
    return pow(x,3)-x-1

def G(x):
    return pow((1+x),1/3)

a=1
b=2
E=1e-2
x=G(a)
k=0

while(abs(F(x))>E):
   x=G(x)
   k+=1
   
   

print("X : ", x, end='\n')
print("k : ", k, end="\n ")

