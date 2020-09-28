# importing required library 
from prettytable import PrettyTable 
  
# creating an empty PrettyTable 
x = PrettyTable() 
  
# adding data into the table 
# row by row 
x.field_names = ["First name", "Last name", "Salary", "City", "DOB"] 
x.add_row(["Shubham", "Chauhan", 60000, "Lucknow", "22 Feb 1999"]) 
x.add_row(["Saksham", "Chauhan", 50000, "Hardoi", "21 Aug 2000"]) 
x.add_row(["Preeti", "Singh", 40000, "Unnao", "10 Jan 1995"]) 
x.add_row(["Ayushi", "Chauhan", 65000, "Haridwar", "30 Jan 2002"]) 
x.add_row(["Abhishek", "Rai", 70000, "Greater Noida", "16 Jan 1999"]) 
x.add_row(["Dinesh", "Pratap", 80000, "Delhi", "3 Aug 1998"]) 
x.add_row(["Chandra", "Kant", 85000, "Ghaziabad", "18 Sept 1997"]) 
  
# printing generated table 
print(x)