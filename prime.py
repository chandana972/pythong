a=input("enter the values:")
b=input("enter the values:")
for i in range(a,b + 1):
   if i > 1:
       for j in range(2,i):
           if (i % 2) == 0:
               break
       else:
           print(i)

