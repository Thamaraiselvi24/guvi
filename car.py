source=int(input("Enter the source km:"))
destination=int(input("Enter the destination km:"))
i=1
km=destination - source
while(i>0):
  car=input("Enter the type of car:")
  if(car=='mini'):
    pay=km * 10
    print(pay)
    i=0
    
  elif(car=='micro'):
    pay=km * 20
    print(pay)
    i=0
  elif(car=='prime'):
    pay=km * 40
    print(pay)
    i=0
  else:
    print("Enter a valid car name")
i=2
while(i>1):
  d=input("do you want to continue")
  i=1
  if(d=='yes'):
    print("continue process")
  elif(d=='no'):
    print("exit")
  else:
    print("invalid keyword")