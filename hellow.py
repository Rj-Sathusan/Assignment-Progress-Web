import streamlit as st
# import required modules
import mysql.connector


# create connection object
mydb  = mysql.connector.connect(
  host=st.secrets["db_host"], user=st.secrets["db_user"],
  password=st.secrets["db_pass"], database=st.secrets["db"])
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM assignment_details")

Result = mycursor.fetchall()

st.write(Result)
