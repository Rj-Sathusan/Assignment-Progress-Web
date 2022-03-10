import streamlit as st
from PIL import Image
import mysql.connector
img = Image.open("Medal.gif")
st.image(img, width=200)

mydb  = mysql.connector.connect(
  host=st.secrets["db_host"], user=st.secrets["db_user"],
  password=st.secrets["db_pass"], database=st.secrets["db"])
  

name = st.text_input("Enter Your Student ID") 
if(st.button('Submit')):
  sql = "SELECT * FROM assignment_details WHERE Student_code="+name

mycursor = mydb.cursor()
mycursor.execute(sql)
Result = mycursor.fetchall()

st.write('Student ID : ',Result[0][0])
st.write(' Name : ',Result[0][1])
st.write('Starting Date : ',Result[0][2])
st.write('Completed Assignments : ',Result[0][3])

if Result[0][3]>14:
        st.write("Statue : Completed")
elif Result[0][3]<14:
        st.write("Statue : ",(15-Result[0][3]),"more assignments pending...")

