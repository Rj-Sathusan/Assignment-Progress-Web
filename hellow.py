import streamlit as st
# import required modules
import mysql.connector
  
# create connection object
mydb  = mysql.connector.connect(
  host=st.secrets[db_host], user="sql6474318",
  password="Q3Bq46Z4Vd", database="sql6474318")
  

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Try")

Result = mycursor.fetchall()
st.write(Result)
