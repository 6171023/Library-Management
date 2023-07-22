import mysql.connector as sqltor
from datetime import date
today = date.today()
mycon=sqltor.connect(host="localhost", user="root", passwd="grade12", database="library")
if mycon.is_connected:
	print("Database access granted!")
else:
	print("Database access denied!!")
cursor=mycon.cursor()

def bookdisplay():
        query="Select*from BookDetails"
        cursor.execute(query)
        records=cursor.fetchall()
        print("\n")
        print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
        print("| BOOK ID | \t  BOOK NAME \t  |   BOOK AUTHOR   |    BOOK PUBLISHER    | BORROW TIME | BOOK FEE |")
        print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
        for record in records:
                print("|",record[0]," "*(6-len(str(record[0]))),"|",
                      record[1]," "*(20-len(record[1])),"|",
                      record[2]," "*(14-len(record[2])),"|",
                      record[3]," "*(19-len(record[3])),"|",
                      record[4]," "*(10-len(str(record[4]))),"|",
                      record[5]," "*(7-len(str(record[5]))),"|")
        print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")

def memdisplay():
        query="Select*from MemberDetails"
        cursor.execute(query)
        records=cursor.fetchall()
        print("\n")
        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
        print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
        for record in records:
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(18-len(record[1])),"|",
                      record[2]," "*(43-len(record[2])),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(21-len(record[4])),"|",
                      record[5]," "*(10-len(str(record[5]))),"|")
        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
        
def borrowdisplay():
        query="Select*from BorrowDetails"
        cursor.execute(query)
        records=cursor.fetchall()
        print("\n")
        print("+-----------+---------+--------------+---------------+---------+")
        print("| MEMBER ID | BOOK ID |  ISSUE DATE  |  RETURN DATE  |   FEE   |")
        print("+-----------+---------+--------------+---------------+---------+")
        for record in records:
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(6-len(str(record[1]))),"|",
                      record[2]," "*(11-len(str(record[2]))),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(6-len(str(record[4]))),"|")
        print("+-----------+---------+--------------+---------------+---------+")
            
def lib2():
        query1 = "Select BookID from BookDetails"
        cursor.execute(query1)
        records = cursor.fetchall()
        print("\n")
        print("These are existing book IDs:")
        for record in records:
                print(record[0])
        print("\n")
        bid = int(input("Enter unique book ID:"))
        name = input("Enter book name:")
        author = input("Enter book author:")
        pub = input("Enter book publisher:")
        time = int(input("Enter the number of days for which the book can be borrowed:"))
        fee = int(input("Enter fee to be paid if book is returned late:"))
        query2 = "Insert into BookDetails(BookID,BookName,BookAuthor,BookPublisher,BorrowTime,BookFee) values{}".format((bid,name,author,pub,time,fee))
        cursor.execute(query2)
        mycon.commit()
        print("\n")
        choice = input("Do you want to see modified table? (y/n):")
        if choice=="y" or choice=="Y":
                bookdisplay()

def lib3():
        print("\n")
        bookID = int(input("Enter the book ID whose records are to be deleted:"))
        query1 = "Delete from BookDetails where BookID={}".format(bookID)
        cursor.execute(query1)
        mycon.commit()
        print("\n")
        choice = input("Do you want to see modified table? (y/n):")
        if choice=="y" or choice=="Y":
                bookdisplay()

def lib4i():
        bid = int(input("Enter book ID whose book name is to be changed:"))
        query1 = "Select * from BookDetails where BookID={}".format(bid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given book ID has following details:")
                print("\n")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("| BOOK ID | \t  BOOK NAME \t  |   BOOK AUTHOR   |    BOOK PUBLISHER    | BORROW TIME | BOOK FEE |")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("|",record[0]," "*(6-len(str(record[0]))),"|",
                      record[1]," "*(20-len(record[1])),"|",
                      record[2]," "*(14-len(record[2])),"|",
                      record[3]," "*(19-len(record[3])),"|",
                      record[4]," "*(10-len(str(record[4]))),"|",
                      record[5]," "*(7-len(str(record[5]))),"|")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("\n")
                new = input("Enter new book name:")
                query2 = "Update BookDetails set BookName='{}' where BookID={}".format(new,bid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                choice = input("Do you want to see modified table? (y/n):")
                if choice=="y" or choice=="Y":
                        bookdisplay()

def lib4ii():
        bid = int(input("Enter book id whose book author is to be changed:"))
        query1 = "Select * from BookDetails where BookID={}".format(bid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given book ID has following details:")
                print("\n")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("| BOOK ID | \t  BOOK NAME \t  |   BOOK AUTHOR   |    BOOK PUBLISHER    | BORROW TIME | BOOK FEE |")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("|",record[0]," "*(6-len(str(record[0]))),"|",
                      record[1]," "*(20-len(record[1])),"|",
                      record[2]," "*(14-len(record[2])),"|",
                      record[3]," "*(19-len(record[3])),"|",
                      record[4]," "*(10-len(str(record[4]))),"|",
                      record[5]," "*(7-len(str(record[5]))),"|")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("\n")
                new = input("Enter new book author:")
                query2 = "Update BookDetails set BookAuthor='{}' where BookID={}".format(new,bid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                choice = input("Do you want to see modified table? (y/n):")
                if choice=="y" or choice=="Y":
                        bookdisplay()

def lib4iii():
        bid = int(input("Enter book id whose book publisher details is to be changed:"))
        query1 = "Select * from BookDetails where BookID={}".format(bid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given book ID has following details:")
                print("\n")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("| BOOK ID | \t  BOOK NAME \t  |   BOOK AUTHOR   |    BOOK PUBLISHER    | BORROW TIME | BOOK FEE |")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("|",record[0]," "*(6-len(str(record[0]))),"|",
                      record[1]," "*(20-len(record[1])),"|",
                      record[2]," "*(14-len(record[2])),"|",
                      record[3]," "*(19-len(record[3])),"|",
                      record[4]," "*(10-len(str(record[4]))),"|",
                      record[5]," "*(7-len(str(record[5]))),"|")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("\n")
                new = input("Enter new book publisher:")
                query2 = "Update BookDetails set BookPublisher='{}' where BookID={}".format(new,bid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                choice = input("Do you want to see modified table? (y/n):")
                if choice=="y" or choice=="Y":
                        bookdisplay()

def lib4iv():
        bid = int(input("Enter book id whose borrow time is to be changed:"))
        query1 = "Select * from BookDetails where BookID={}".format(bid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given book ID has following details:")
                print("\n")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("| BOOK ID | \t  BOOK NAME \t  |   BOOK AUTHOR   |    BOOK PUBLISHER    | BORROW TIME | BOOK FEE |")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("|",record[0]," "*(6-len(str(record[0]))),"|",
                      record[1]," "*(20-len(record[1])),"|",
                      record[2]," "*(14-len(record[2])),"|",
                      record[3]," "*(19-len(record[3])),"|",
                      record[4]," "*(10-len(str(record[4]))),"|",
                      record[5]," "*(7-len(str(record[5]))),"|")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("\n")
                new = input("Enter new borrow time:")
                query2 = "Update BookDetails set BorrowTime='{}' where BookID={}".format(new,bid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                choice = input("Do you want to see modified table? (y/n):")
                if choice=="y" or choice=="Y":
                        bookdisplay()

def lib4v():
        bid = int(input("Enter book id whose fee is to be changed:"))
        query1 = "Select * from BookDetails where BookID={}".format(bid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given book ID has following details:")
                print("\n")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("| BOOK ID | \t  BOOK NAME \t  |   BOOK AUTHOR   |    BOOK PUBLISHER    | BORROW TIME | BOOK FEE |")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("|",record[0]," "*(6-len(str(record[0]))),"|",
                      record[1]," "*(20-len(record[1])),"|",
                      record[2]," "*(14-len(record[2])),"|",
                      record[3]," "*(19-len(record[3])),"|",
                      record[4]," "*(10-len(str(record[4]))),"|",
                      record[5]," "*(7-len(str(record[5]))),"|")
                print("+---------+-----------------------+-----------------+----------------------+-------------+----------+")
                print("\n")
                new = input("Enter new fee:")
                query2 = "Update BookDetails set BookFee='{}' where BookID={}".format(new,bid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                choice = input("Do you want to see modified table? (y/n):")
                if choice=="y" or choice=="Y":
                        bookdisplay()

def lib4menu():
        choice="y"
        while choice=="y" or choice=="Y":
                print("\n")
                print("1) BookName")
                print("2) BookAuthor")
                print("3) BookPublisher")
                print("4) BorrowTime")
                print("5) BookFee")
                print("\n")
                option = input("Enter update menu option to be executed:")
                print("\n")
                if option=="1":
                        lib4i()
                elif option=="2":
                        lib4ii()
                elif option=="3":
                        lib4iii()
                elif option=="4":
                        lib4iv()
                elif option=="5":
                        lib4v()
                else:
                        print("Invalid input.")
                print("\n")
                choice=input("Do you want to continue updating?(y/n):")

def librarian():
        choice="y"
        while choice=="y" or choice=="Y":
                print("\n")
                print("LIBRARIAN MENU OPTIONS:")
                print("1) Display book details")
                print("2) Add book")
                print("3) Delete book")
                print("4) Update book details")
                print("5) View borrowed book details")
                print("6) View member details")
                print("\n")
                option = input("Enter menu option to be executed:")
                if option=="1":
                        bookdisplay()
                elif option=="2":
                        lib2()
                elif option=="3":
                        lib3()
                elif option=="4":
                        lib4menu()
                elif option=="5":
                        borrowdisplay()
                elif option=="6":
                        memdisplay()
                else:
                        print("Invalid input.")
                print("\n")
                choice=input("Do you want to continue with any other option?(y/n):")

def mem2():
        query1 = "Select MemberID from MemberDetails"
        cursor.execute(query1)
        records = cursor.fetchall()
        print("\n")
        print("These are existing Member IDs:")
        for record in records:
                print(record[0])
        print("\n")
        mid = input("Enter unique member ID that starts with a letter and ends with two digits:")
        name = input("Enter your name:")
        addr = input("Enter your address:")
        phno = int(input("Enter your phone number:"))
        mail = input("Enter your email address:")
        query2 = "Insert into MemberDetails(MemberID,MemberName,MemberAddress,MemberNo,MemberEmail,DateJoined) values{}".format((mid,name,addr,phno,mail,str(today)))
        cursor.execute(query2)
        mycon.commit()
        print("\n")
        print("Congratulations! You have become a new member!")

def mem3():
        print("\n")
        mid = input("Enter your member ID:")
        query1 = "Select * from MemberDetails where MemberID='{}'".format(mid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given member ID has following details:")
                print("\n")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(18-len(record[1])),"|",
                      record[2]," "*(43-len(record[2])),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(21-len(record[4])),"|",
                      record[5]," "*(10-len(str(record[5]))),"|")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
        print("\n")
        query2 = "Select * from BorrowDetails where MemberID='{}'".format(mid)
        cursor.execute(query2)
        records = cursor.fetchall()
        if records==[]:
                print("No history of borrowed books available.")
        else:
                print("Borrowed book details:")
                print("\n")
                print("+-----------+---------+--------------+---------------+---------+")
                print("| MEMBER ID | BOOK ID |  ISSUE DATE  |  RETURN DATE  |   FEE   |")
                print("+-----------+---------+--------------+---------------+---------+")
                for record in records:
                        print("|",record[0]," "*(8-len(record[0])),"|",
                              record[1]," "*(6-len(str(record[1]))),"|",
                              record[2]," "*(11-len(str(record[2]))),"|",
                              record[3]," "*(12-len(str(record[3]))),"|",
                              record[4]," "*(6-len(str(record[4]))),"|")
                print("+-----------+---------+--------------+---------------+---------+")

def mem4i():
        mid = input("Enter your member ID:")
        query1 = "Select * from MemberDetails where MemberID='{}'".format(mid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given member ID has following details:")
                print("\n")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(18-len(record[1])),"|",
                      record[2]," "*(43-len(record[2])),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(21-len(record[4])),"|",
                      record[5]," "*(10-len(str(record[5]))),"|")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("\n")
                new = input("Enter new name:")
                query2 = "Update MemberDetails set MemberName='{}' where MemberID='{}'".format(new,mid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                query3 = "Select * from MemberDetails where MemberID='{}'".format(mid)
                cursor.execute(query3)
                record1 = cursor.fetchone()
                choice = input("Do you want to see your modified record? (y/n):")
                print("\n")
                if choice=="y" or choice=="Y":
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("|",record1[0]," "*(8-len(record1[0])),"|",
                              record1[1]," "*(18-len(record1[1])),"|",
                              record1[2]," "*(43-len(record1[2])),"|",
                              record1[3]," "*(12-len(str(record1[3]))),"|",
                              record1[4]," "*(21-len(record1[4])),"|",
                              record1[5]," "*(10-len(str(record1[5]))),"|")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")

def mem4ii():
        mid = input("Enter your member ID:")
        query1 = "Select * from MemberDetails where MemberID='{}'".format(mid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given member ID has following details:")
                print("\n")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(18-len(record[1])),"|",
                      record[2]," "*(43-len(record[2])),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(21-len(record[4])),"|",
                      record[5]," "*(10-len(str(record[5]))),"|")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("\n")
                new = input("Enter new address:")
                query2 = "Update MemberDetails set MemberAddress='{}' where MemberID='{}'".format(new,mid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                query3 = "Select * from MemberDetails where MemberID='{}'".format(mid)
                cursor.execute(query3)
                record1 = cursor.fetchone()
                choice = input("Do you want to see your modified record? (y/n):")
                print("\n")
                if choice=="y" or choice=="Y":
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("|",record1[0]," "*(8-len(record1[0])),"|",
                              record1[1]," "*(18-len(record1[1])),"|",
                              record1[2]," "*(43-len(record1[2])),"|",
                              record1[3]," "*(12-len(str(record1[3]))),"|",
                              record1[4]," "*(21-len(record1[4])),"|",
                              record1[5]," "*(10-len(str(record1[5]))),"|")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")

def mem4iii():
        mid = input("Enter your member ID:")
        query1 = "Select * from MemberDetails where MemberID='{}'".format(mid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given member ID has following details:")
                print("\n")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(18-len(record[1])),"|",
                      record[2]," "*(43-len(record[2])),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(21-len(record[4])),"|",
                      record[5]," "*(10-len(str(record[5]))),"|")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("\n")
                new = int(input("Enter new phone number:"))
                query2 = "Update MemberDetails set MemberNo={} where MemberID='{}'".format(new,mid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                query3 = "Select * from MemberDetails where MemberID='{}'".format(mid)
                cursor.execute(query3)
                record1 = cursor.fetchone()
                choice = input("Do you want to see your modified record? (y/n):")
                print("\n")
                if choice=="y" or choice=="Y":
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("|",record1[0]," "*(8-len(record1[0])),"|",
                              record1[1]," "*(18-len(record1[1])),"|",
                              record1[2]," "*(43-len(record1[2])),"|",
                              record1[3]," "*(12-len(str(record1[3]))),"|",
                              record1[4]," "*(21-len(record1[4])),"|",
                              record1[5]," "*(10-len(str(record1[5]))),"|")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")

def mem4iv():
        mid = input("Enter your member ID:")
        query1 = "Select * from MemberDetails where MemberID='{}'".format(mid)
        cursor.execute(query1)
        record = cursor.fetchone()
        print("\n")
        if record==None:
                print("No such record exists.")
        else:
                print("The given member ID has following details:")
                print("\n")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("|",record[0]," "*(8-len(record[0])),"|",
                      record[1]," "*(18-len(record[1])),"|",
                      record[2]," "*(43-len(record[2])),"|",
                      record[3]," "*(12-len(str(record[3]))),"|",
                      record[4]," "*(21-len(record[4])),"|",
                      record[5]," "*(10-len(str(record[5]))),"|")
                print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                print("\n")
                new = input("Enter new email:")
                query2 = "Update MemberDetails set MemberEmail='{}' where MemberID='{}'".format(new,mid)
                cursor.execute(query2)
                mycon.commit()
                print("\n")
                query3 = "Select * from MemberDetails where MemberID='{}'".format(mid)
                cursor.execute(query3)
                record1 = cursor.fetchone()
                choice = input("Do you want to see your modified record? (y/n):")
                print("\n")
                if choice=="y" or choice=="Y":
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("| MEMBER ID |     MEMBER NAME     | \t\t    MEMBER ADDRESS    \t\t | MEMBER NUMBER | \t MEMBER EMAIL \t  | DATE JOINED |")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")
                        print("|",record1[0]," "*(8-len(record1[0])),"|",
                              record1[1]," "*(18-len(record1[1])),"|",
                              record1[2]," "*(43-len(record1[2])),"|",
                              record1[3]," "*(12-len(str(record1[3]))),"|",
                              record1[4]," "*(21-len(record1[4])),"|",
                              record1[5]," "*(10-len(str(record1[5]))),"|")
                        print("+-----------+---------------------+----------------------------------------------+---------------+------------------------+-------------+")

def mem4menu():
        choice="y"
        while choice=="y" or choice=="Y":
                print("\n")
                print("1) MemberName")
                print("2) MemberAddress")
                print("3) MemberNo")
                print("4) MemberEmail")
                print("\n")
                option = input("Enter update menu option to be executed:")
                print("\n")
                if option=="1":
                        mem4i()
                elif option=="2":
                        mem4ii()
                elif option=="3":
                        mem4iii()
                elif option=="4":
                        mem4iv()
                elif option=="5":
                        mem4v()
                else:
                        print("Invalid input.")
                print("\n")
                choice=input("Do you want to continue updating?(y/n):")

def mem5():
        print("\n")
        mid = input("Enter your member ID:")
        query1 = "Select * from MemberDetails where MemberID='{}'".format(mid)
        cursor.execute(query1)
        record = cursor.fetchone()
        if record==None:
                print("\n")
                print("No such record exists.")
        else:
                print("\n")
                print("These are the following books available:")
                bookdisplay()
                print("\n")
                bid = int(input("Enter book ID of book to be issued:"))
                issuedate = str(today)
                query1 = "Insert into BorrowDetails(MemberID,BookID,IssueDate) values{}".format((mid,bid,str(issuedate)))
                cursor.execute(query1)
                mycon.commit()
                print("\n")
                query2 = "Select * from BorrowDetails where MemberID='{}' and BookID={}".format(mid,bid)
                cursor.execute(query2)
                record = cursor.fetchone()
                choice = input("Do you want to see your modified record? (y/n):")
                if choice=="y" or choice=="Y":
                        print("\n")
                        print("+-----------+---------+--------------+---------------+---------+")
                        print("| MEMBER ID | BOOK ID |  ISSUE DATE  |  RETURN DATE  |   FEE   |")
                        print("+-----------+---------+--------------+---------------+---------+")
                        print("|",record[0]," "*(8-len(record[0])),"|",
                              record[1]," "*(6-len(str(record[1]))),"|",
                              record[2]," "*(11-len(str(record[2]))),"|",
                              record[3]," "*(12-len(str(record[3]))),"|",
                              record[4]," "*(6-len(str(record[4]))),"|")
                        print("+-----------+---------+--------------+---------------+---------+")
        
def mem6():
        print("\n")
        mid = input("Enter your member ID:")
        query1 = "Select * from BorrowDetails where MemberID='{}' and ReturnDate is null".format(mid)
        cursor.execute(query1)
        records = cursor.fetchall()
        condition = 0
        for record in records:
                record=list(record)
                date = record[3]
                date = str(date)
                if date=="None":
                        condition = 1
                        print("\n")
                        mid = record[0]
                        bid = record[1]
                        returndate = str(today)
                        query2 = "Update BorrowDetails set ReturnDate='{}' where MemberID='{}' and BookID={}".format(returndate,mid,bid)
                        cursor.execute(query2)
                        mycon.commit()
                        print("Book returned.")
                        query3 = "Select * from BorrowDetails where MemberID='{}' and BookID={}".format(mid,bid)
                        cursor.execute(query3)
                        record = cursor.fetchone()
                        difference = record[3]-record[2]
                        time = difference.days
                        query4 = "Select * from BookDetails where BookID={}".format(bid)
                        cursor.execute(query4)
                        bookrec = cursor.fetchone()
                        borrowtime = bookrec[4]
                        bookfee = bookrec[5]
                        if time>borrowtime:
                                fee = (time-borrowtime)*bookfee
                        else:
                                fee=0
                        query5 = "Update BorrowDetails set Fee={} where MemberID='{}' and BookID={}".format(fee,mid,bid)
                        cursor.execute(query5)
                        mycon.commit()
                        print("\n")
                        query6 = "Select * from BorrowDetails where MemberID='{}' and BookID={}".format(mid,bid)
                        cursor.execute(query6)
                        record1 = cursor.fetchone()
                        choice = input("Do you want to see your modified record? (y/n):")
                        if choice=="y" or choice=="Y":
                                print("\n")
                                print("+-----------+---------+--------------+---------------+---------+")
                                print("| MEMBER ID | BOOK ID |  ISSUE DATE  |  RETURN DATE  |   FEE   |")
                                print("+-----------+---------+--------------+---------------+---------+")
                                print("|",record1[0]," "*(8-len(record1[0])),"|",
                                        record1[1]," "*(6-len(str(record1[1]))),"|",
                                        record1[2]," "*(11-len(str(record1[2]))),"|",
                                        record1[3]," "*(12-len(str(record1[3]))),"|",
                                        record1[4]," "*(6-len(str(record1[4]))),"|")
                                print("+-----------+---------+--------------+---------------+---------+")
                else:
                        condition = 0
        if condition==0:
                print("\n")
                print("No such records exist.")

def member():
        choice="y"
        while choice=="y" or choice=="Y":
                print("\n")
                print("MEMBER MENU OPTIONS:")
                print("1) View book details")
                print("2) Register yourself")
                print("3) Display your details")
                print("4) Update your details")
                print("5) Issue book")
                print("6) Return book")
                print("\n")
                option = input("Enter menu option to be executed:")
                if option=="1":
                        bookdisplay()
                elif option=="2":
                        mem2()
                elif option=="3":
                        mem3()
                elif option=="4":
                        mem4menu()
                elif option=="5":
                        mem5()
                elif option=="6":
                        mem6()
                else:
                        print("\n")
                        print("Invalid input.")
                print("\n")
                choice=input("Do you want to continue with any other option?(y/n):")

def first():
        print("\n")
        print("Are you a librarian or a member?")
        status = input("Enter 'L' for librarian or 'M' for member:")
        while len(status)!=0:
                if status=="L" or status=="l":
                        librarian()
                        break
                elif status=="M" or status=="m":
                        member()
                        break
                else:
                        print("Invalid input. Please re-enter status.")
                        status = input("Enter 'L' for librarian or 'M' for member:")
        mycon.close()
first()
