print("select your ride: ")
print("1. bike")
print("2. car")

choice = int(input("enter your choice: "))

if( choice == 1 ):
    print( "what type of bike? " )
    print("1. scooty\n")
    print("2. scooter\n")

    choice2=int(input("enter choice 2: "))
    if choice2==1:
       print("you chose scooty")
    else:
       print("you chose scooter")

elif( choice == 2 ):
   print("what type of car?")
   print("1.seadan")
   print("2.xuv")
   choice3=int(input("enter choice 3: "))
   if choice3==1:
      print("you chose sedan")
   else:
      print("you chose xuv")

else:
  print("wrong choice!!!!")