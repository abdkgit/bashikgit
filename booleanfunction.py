def isdivisible(x,y):
  if x%y==1:
     result= True
  else:
    result= False
  return result 
a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
print(isdivisible(a,b))

