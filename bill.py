import mysql.connector
from tabulate import tabulate
import sys
from datetime import datetime
try:
    mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database=' hoteldb')
except mysql.connector.Error as e:
    #print("connection error")   
    sys.exit("dbconnection failure")
mycursor= mydb.cursor()
total=0
items=[]
while True:
    print("select an option from the menu")
    print("1. Tea:----------10rs")
    print("2.Cofee:---------15rs")
    print("3.Chips:----------20rs")
    print("4.Sandwitch:------30rs")
    print("6.Generate  Bill----")
    print("7.View all transaction----")
    print("8.Day wise transaction summery----")
    print("9.Transaction summery for a period----")
    print("10.Exit:-")

    choice=int(input("Please enter your choice:-"))
    if(choice==1):
        print("Tea added")
        quantity=int(input("enter the quantity:--"))
        total+=10*quantity
        items.append("tea "+str(quantity))
        #print("quantity=",quantity)
        #print("total=",total)
    elif(choice==2):
        print("Cofee added")
        quantity=int(input("enter the quantity:--"))
        total+=15*quantity
        items.append("cofee "+str(quantity))
        #print("quantity=",quantity)
        #print("total=",total)
    elif(choice==3):
        print("Chips added")
        quantity=int(input("enter the quantity:--"))
        total+=20*quantity
        items.append("chips "+str(quantity))
        #print("quantity=",quantity)
        #print("total=",total)
    elif(choice==4):
        print("Sandwitch added")
        quantity=int(input("enter the quantity:--"))
        total+=30*quantity
        items.append("sandwitch "+str(quantity))
        #print("quantity=",quantity)
        #print("total=",total)
    elif(choice==6):
        name=input("enter your name:--")
        phone=input("enter your phone:--")
        print("****bill****")
        print("Name:-",name)
        print("phone:-",phone)
        date= datetime.today().strftime('%Y-%m-%d')
        print("date:-",date)
        print("****items*****")
        for i in items:
            print(i)
        print("total bill =",total)
        try:
            sql="INSERT INTO `bill`(`name`, `phone`, `date`, `amount`) VALUES (%s,%s,now(),%s)"
            data=(name,phone,total)
            mycursor.execute(sql,data)
            mydb.commit()
        except mysql.connector.Error as e:
            sys.exit("insert error")

        items=[]
        total=0
    elif(choice==7):
        print("view all transaction") 
        date=input("enter a date(yy-mm-dd):-")
        try:
            sql="SELECT `name`, `phone`, `amount` FROM `bill` WHERE `date`='"+date+"'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(tabulate(result,headers=["name","phone","amount"],tablefmt="psql")) 
        except mysql.connector.Error as e:
            sys.exit("view transaction error")    

    elif(choice==8):
        print("display transaction sumery of particulr date") 
        date=input("enter a date(yy-mm-dd):-")
        try:
            sql="SELECT `name`, `phone`, `amount` FROM `bill` WHERE `date`='"+date+"'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(tabulate(result,headers=["name","phone","amount"],tablefmt="psql" ))
        except mysql.connector.Error  as e:
            sys.exit("transaction summery error")  
    elif(choice==9):
        print("Transaction sumery of period")
        date1=input("enter a statring date(yy-mm-dd):-")
        date2=input("enter a  end date(yy-mm-dd):-")
        try:
            sql="SELECT SUM(`amount`) FROM `bill` WHERE `date` BETWEEN '"+date1+"' AND '"+date1+"' "
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(tabulate(result,headers=["amount"],tablefmt="psql" ))
        except mysql.connector.Error as e:
            sys.exit("ransaction summery between 2 dates")    
    elif(choice==10):
        break    

  