a=input("enter string")
b=[]
for i in a:
    if i not in b:
       b.append(i)
       print(i,a.count(i))
