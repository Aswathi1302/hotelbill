import mysql.connector
mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database=' hoteldb')
mycursor= mydb.cursor()
total=0
items=[]
while True:
    print("select an option from the menu")
    print("1. Tea:-")
    print("2.Cofee:-")
    print("3.Chips:-")
    print("4.Sandwitch:-")
    print("5.cake:-")
    print("6.Generate  Bill:-")
    print("7.Exit:-")

    choice=int(input("Please enter your choice:-"))
    if(choice==1):
        print("Tea added")
        quantity=int(input("enter the quantity"))
        total+=10*quantity
        items.append("tea "+str(quantity))
        print("quantity=",quantity)
        print("total=",total)
    elif(choice==2):
        print("Cofee added")
    elif(choice==3):
        print("Chips added")
    elif(choice==4):
        print("Sandwitch added")
    elif(choice==5):
        print("Cake added")
    elif(choice==6):
        name=input("enter your name")
        #phone=input("enter your phone")
        #date=imput("enter the date")
       #sql="INSERT INTO `bill`(`name`, `phone`, `date`, `amount`) VALUES (%s,%s,%s,%s)"
       #data=(name,phone,date)
        #print("bill")
    elif(choice==7):
        break    

  