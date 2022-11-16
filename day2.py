import pdb
def add(a,b):
    answer=a*b
    return answer
pdb.set_trace()
x=int(input("enter first number"))
y=int(input("enter second number"))
sum=add(x,y)
print(sum)