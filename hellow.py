import streamlit as st
# import required modules
import mysql.connector


# create connection object
mydb  = mysql.connector.connect(
  host=st.secrets["db_host"], user=st.secrets["db_user"],
  password=st.secrets["db_pass"], database=st.secrets["db"])
  

mycursor = mydb.cursor()

sql = "SELECT * FROM assignment_details WHERE Student_code=1003"
mycursor.execute(sql)
#mycursor.execute("SELECT * FROM assignment_details")

Result = mycursor.fetchall()

n=('Student ID : ',Result[0][0],'\nName : ',Result[0][1],'\nStarting Date : ',Result[0][2],'\nCompleted Assignments : ',Result[0][3])
st.write(n)

if Result[0][3]>14:
        st.write("Statue : Completed")
elif Result[0][3]<14:
        st.write("Statue : ",(15-Result[0][3]),"more pending...")

