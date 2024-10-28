from prettytable import PrettyTable
import mysql.connector
from prettytable import prettytable

mydb=mysql.connector.connect(host="localhost",
user="root",
passwd="ronaldoo",
database="school")
mycursor=mydb.cursor()
print("------------------------------------MAIN MENU-----------------------------------")
def stuInsert():
  L=[]
  roll=int(input("Enter the roll number : "))
  L.append(roll)
  name=input("Enter the Name: ")
  L.append(name)
  age=int(input("Enter Age of Student : "))
  L.append(age)
  classs=input("Enter the Class : ")
  L.append(classs)
  city=input("Enter the City ofthe Student : ")
  L.append(city)
  stud=(L)
  sql="insert into student (roll,name,age,class,city) values (%s,%s,%s,%s,%s)"
  mycursor.execute(sql,stud)
  mydb.commit()
  print("inserted successfully")
def stuView():
  print("Select the search criteria : ")
  print("1. Roll")
  print("2. Name")
  print("3. Age")
  print("4. City")
  print("5. All")
  ch=int(input("Enter the choice : "))
  if ch==1:
    s=int(input("Enter roll no : "))
    rl=(s,)
    sql="select * from student where roll=%s"
    mycursor.execute(sql,rl)
  elif ch==2:
    s=input("Enter Name : ")
    rl=(s,)
    sql="select * from student where name=%s"
    mycursor.execute(sql,rl)
  elif ch==3:
    s=int(input("Enter age : "))
    rl=(s,)
    sql="select * from student where age=%s"
    mycursor.execute(sql,rl)
  elif ch==4:
    s=input("Enter City : ")
    rl=(s,)
    sql="select * from student where City=%s"
    mycursor.execute(sql,rl)
  elif ch==5:
    sql="select * from student"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class, City)")
    t=PrettyTable(['ROLL','NAME', 'AGE', 'CLASS', 'CITY'])
    for roll, name, age, classs, city in res:
      t.add_row([roll, name, age, classs, city])
    print(t)
def feeDeposit():
  L=[]
  roll=int(input("Enter the roll number : "))
  L.append(roll)
  feeDeposit=int(input("Enter the Fee to be deposited : "))
  L.append(feeDeposit)
  month=input("Enter month of fee : ")
  L.append(month)
  fee=(L)
  sql="insert into fee (roll,feeDeposit,Month) values (%s,%s,%s)"
  mycursor.execute(sql,fee)
  mydb.commit()
  print("inserted successfully")
def feeView():
  print("Please enter the details to view the fee details :")
  roll=int(input("Enter the roll number of the student whose fee is to be viewed : "))
  sql="Select Student.Roll, Student.Name, Student.Class, fee.feeDeposit, fee.month from Student INNER JOIN fee ON Student.roll=fee.roll and fee.roll = %s" % (roll)
  mycursor.execute(sql)
  res=mycursor.fetchall()
  mydb.commit()
  print("The Students fees details are as follows \n: ")
  t=PrettyTable(['ROLL','NAME', 'CLASS', 'FEES', 'MONTH'])
  for roll, name, classs, fees, month in res:
      t.add_row([roll, name, classs, fees, month])
  print(t)
def removeStu():
   roll=int(input("Enter the roll number of the student to be deleted : "))
   rl=(roll,)
   sql="Delete from fee where roll=%s"
   mycursor.execute(sql,rl)
   sql="Delete from Student where roll=%s"
   mycursor.execute(sql,rl)
   mydb.commit()

def RunAgain():
  ch=str(input("do you want to run again y or n \n"))
  if ch=='y':
    print("------------------------------------MAIN MENU-----------------------------------")
    MenuSet()
  
while(1):
  def MenuSet(): 
   print("Enter 1 : To Add Student")
   print("Enter 2 : To View Student ")
   print("Enter 3 : To Deposit Fee ")
   print("Enter 4 : To Remove Student")
   print("Enter 5 : To View Fee of Any Student")
   try: 
     userInput = int(input("Please Select An Above Option: "))
   except ValueError:
     exit("\nHey! That's a Wrong choice Try again")
     
   else:
     print("\n") 
     if(userInput == 1):
        stuInsert()
        RunAgain()
     elif(userInput==2):
        stuView()
        RunAgain()
     elif(userInput==3):
        feeDeposit()
        RunAgain()
     elif(userInput==4):
        removeStu()
        RunAgain()
     elif(userInput==5):
        feeView()
        RunAgain()
     else:
       print("wrong choice\n")
       print("Enter correct choice. . . ")
       print("------------------------------------MAIN MENU-----------------------------------")
  MenuSet()

  

