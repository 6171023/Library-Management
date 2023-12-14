# Library-Management

A Python+MySQL project to create an application level library management system.
In summary, the program does the following:

MySQL:
- Creating a table for details regarding borrowing details
- Creating a table to store member details 
- Creating a table to store book details
- MemberID and BookID from member details table and book details table are stored in the borrow details table

Python:
- Uses mysql.connector to connect with MySQL database
- Has 2 interfaces - one for librarian user, one for member user
- For librarian:
   - Allows options to display, add, delete and update book details, view borrowed book details, view member details
- For member:
   - Allows options to view book details, user registration, displaying and updating user details, issuing books from available books to borrow, returning books
