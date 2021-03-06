import streamlit as st
from PIL import Image
import mysql.connector


st.markdown("<h4 style='text-align: center; color: white;'>IDM    Eastern Campues</h4><u><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

mydb  = mysql.connector.connect(
  host=st.secrets["db_host"], user=st.secrets["db_user"],
  password=st.secrets["db_pass"], database=st.secrets["db"])
col1, col2 = st.columns([1,1])

#agree = st.checkbox('I agree',value = True)

#options = st.multiselect(
 #   "What are your favorite colors",
 #   ["Green", "Yellow", "Red", "Blue"],
 #   default=["Yellow"]
#)

with col1:
      who = st.selectbox("I am a",
                     ['Student', 'Teacher'])
with col2:
      name = st.text_input("Enter Your "+who+" ID","") 
if(st.button('Submit')):
  sql = "SELECT * FROM assignment_details WHERE Student_code="+name
  mycursor = mydb.cursor()
  mycursor.execute(sql)
  Result = mycursor.fetchall()
  st.write('')
  

  col1, col2 = st.columns([1,1])
  
  with col1:
        st.write(' Student ID : ',Result[0][0])
        st.write('Name : ',Result[0][1])
        st.write('Starting Date : ',Result[0][2])
        st.write('Completed Assignments : ',Result[0][3])
        if Result[0][3]>14:
          st.write('Congratulations ',(Result[0][1])[2:],' keep going !')
        elif Result[0][3]<14:
          st.write('Never give up ',(Result[0][1])[2:],' keep going !')
   
          
  if Result[0][3]>14:
        with col2:
                st.success("Statue : Completed")
                st.image("https://cdn.dribbble.com/users/43762/screenshots/1097917/dribbble_olympics_medal.gif")
                            
  elif Result[0][3]<14:
        with col2:
                st.write("Statue : ",(15-Result[0][3])," more assignments pending...")
                img = Image.open('pngtree-never-give-up-motivation-poster-concept-black-and-white-illustration-png-image_2154318-removebg-preview.png')
                st.image(img, width=300)
                
                


 
  
 


       





