import streamlit as st
# import required modules
import mysql.connector


# create connection object
mydb  = mysql.connector.connect(
  host="sql6.freemysqlhosting.net", user="sql6474318",
  password="Q3Bq46Z4Vd", database=st.secrets["db"])
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Try")

Result = mycursor.fetchall()

st.write(Result)
