'''
error 1: https://newbedev.com/python-mysql-connector-unread-result-found-when-using-fetchone
'''
from re import X
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="vyas",
  password="password",
  database="library"
)

mycursor = mydb.cursor(buffered=True) #the buffered = true is used because the mycursor is used many places so it throws an error 1

class lib:
    def admin_tool(self,i):
        print("under construction")
        print("you are under admin tool")
        #choices: search book,see dew
        choice=0
        while(choice!=3):
            print("welcome "+i[1])
            print("1.search books 2.manage dew 3.logout")
            choice=int(input("enter your choice:"))
            if(choice==1):
                self.search_books(i)
            if(choice==2):
                self.dew_manage()

        return


    def dew_manage(self):
        choice=0
        while(choice!=4):
            choice=int(input("1.search dew 2.add dew 3.remove dew 4.leave:"))
            if(choice==1):
                n=input("enter user id")
                sql="select * from lib_dew where uid="+n
                mycursor.execute(sql)
                for i in mycursor:
                    print(i)
            elif(choice==2):
                uid=input("enter user id name:")
                bid=input("enter the book id:")
                sql="insert into lib_dew(uid,bid,dborrow,dreturn) values (" + uid+"," + bid + ",now(),DATE_ADD(now(), interval 1 month))" #  " + "\'" + n + "\'"
                mycursor.execute(sql)
                sql="update books set quantity=quantity-1 where bid="+bid
                mycursor.execute(sql)
                mydb.commit()
                print("dew added")
            elif(choice==3):
                did=input("enter user did:")
                sql="select * from lib_dew where did="+did
                mycursor.execute(sql)
                for b in mycursor:
                    bid=str(b[2])
                sql="update books set quantity=quantity+1 where bid="+bid
                mycursor.execute(sql)
                sql = "DELETE FROM lib_dew WHERE did ="+did
                mycursor.execute(sql)
                mydb.commit()
                print("dew removed successfully")
                
        return
    def search_books(self,i):
        mycursor.execute("select * from books")
        choice=0
        while(choice!=4):
            choice=int(input("1.search by id 2.search by name 3.search by author 4.leave:"))
            if(choice==1):
                n=input("enter id")
                sql="select * from books where bid="+n
                mycursor.execute(sql)
                for i in mycursor:
                    print(i)
            elif(choice==2):
                n=input("enter book name:")
                sql="select * from books where uname regexp  " + "\'" + n + "\'"
                mycursor.execute(sql)
                for i in mycursor:
                    print(i)
            elif(choice==3):
                n=input("enter author name:")
                sql="select * from books where author regexp  " + "\'" + n + "\'"
                mycursor.execute(sql)
                for i in mycursor:
                    print(i)
        return
    def check_dew_user(self,i):
        print("under construction")
        return
    def portal(self,i):
        #choices: search book,see dew
        choice=0
        while(choice!=3):
            print("welcome "+i[1])
            print("1.search books 2.check dew 3.logout")
            choice=int(input("enter your choice:"))
            if(choice==1):
                self.search_books(i)
            if(choice==2):
                self.check_dew_user(i)

        return
    def admin_login(self):
        print("under construction")
        username = input("enter name:")
        mycursor.execute("select * from lib_admin")
        auth="nil"
        for i in mycursor:
            if(i[1]==username):
                auth="done"
                password = input("enter password:")
                if(password==i[2]):
                    print("login success")
                    self.admin_tool(i)
                else:
                    print("password incorrect")
                break
        if(auth=="nil"):
            print("username not found")

            return
        auth="nil"

        return 
        
        return 
    def user_login(self):
        username = input("enter name:")
        mycursor.execute("select * from lib_user")
        auth="nil"
        for i in mycursor:
            if(i[1]==username):
                auth="done"
                password = input("enter password:")
                if(password==i[2]):
                    print("login success")
                    self.portal(i)
                else:
                    print("password incorrect")
                break
        if(auth=="nil"):
            print("username not found")

            return
        auth="nil"

        return 

if __name__ == "__main__":

    x=lib()
    choice=0
    while(choice!=3):
        print("POOMPUHAR LIBRARY")
        print("1.user login")
        print("2.admin login")
        print("3.exit")
        choice=int(input("enter a choice"))
        if(choice==1):
            x.user_login()
        elif(choice==2):
            x.admin_login()
        

    