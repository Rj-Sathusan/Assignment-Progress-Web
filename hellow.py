# Python program to create a table

from tkinter import *


class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=15, fg='black',
							font=('Arial',12))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])



# import required modules
import mysql.connector
  
# create connection object
mydb  = mysql.connector.connect(
  host="sql6.freemysqlhosting.net", user="sql6474318",
  password="Q3Bq46Z4Vd", database="sql6474318")
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Try")

Result = mycursor.fetchall()

head=[("ID","NAME")]
lst = head+Result

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[2])

# create root window
root = Tk()
t = Table(root)
root.mainloop()
