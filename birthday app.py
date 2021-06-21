dict={}
while True:
    print("-----------WELCOME TO MY BIRTHDAY APP----------")
    print("1.show birthday")
    print("2.add birthday")
    print("exit")
    choice=int(input("enter your choice"))
    if choice==1:
               if len(dict.keys())==0:
                 print("no birthday")
               else:
                 name=input("enter your name")
                 birthday=dict.get(name,"no data")
                 print(birthday)
    elif choice==2:
               name=input("enter your name")
               date=input("enter your birthday date")
               dict[name]=date
               print("birthday added")
    elif choice==3:
               break
    else:
               print("wrong choice enter")
                     
                           
