import streamlit as st
# import required modules
import mysql.connector
  
# create connection object
mydb  = mysql.connector.connect(
  host=(st.secrets[db_host]), user=(st.secrets[db_username]),
  password=(st.secrets[db_password]), database=(st.secrets[db_username]))
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Try")

Result = mycursor.fetchall()
st.write(Result)
