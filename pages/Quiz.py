import streamlit as st
from PIL import Image

st.title("✨ What Type of Tea Are You? ☕")
 
st.write("Answer the questions below to find out what tea matches your personality!")
 
# Question 1

q1 = st.radio(

    "What flavor profile suits you best?",

    ("Bitter", "Fruity", "Rich & Smooth", "Floral")

)

 
# Question 2

st.write("Which tea latte/s do you prefer?")
q2 = st.selectbox("Pick one", ["Earl Grey Latte", "Matcha Latte", "Chain Tea Latte"])



 
# Question 3

st.write("How many cups of tea would you typically drink in a day?")
q3 = st.slider("Pick an answer:",1, 10)



#Quuestion 4

q4 = st.radio(

    "Choose an animal",

    ("Swan", "Duck", "Shark", "Capybara")
)


#Question 5

st.write("How many cubes of sugar would you put in your tea")
q5=value = st.number_input("Enter your answer:", step=1)


    
 
# Simple result logic (without lists/dicts/session_state)

if st.button("Show My Coffee Personality!"):

    if q1 == "Fruity" or q3 == "Swan":

        st.subheader("☕ You’re a Sencha green tea!")

        st.write("Warm, comforting, and always reliable.")
        
        green_image = Image.open("images2/green.jpeg")
        st.image(green_image, width = 180)

        st.balloons()
 
    elif q1 == "Bitter" or q2 == "Matcha Tea Latte":

        st.subheader("🍵 You’re a Matcha Latte!")

        st.write("Ummami, refreshing, and always a good time.")

        matcha_image = Image.open("images2/matcha.jpeg")
        st.image(matcha_image, width = 180)
 
    elif q1 == "Rich & Smooth" or q4 == "2" or q4 == "3" or q4 == "1" or q4 == "4":

        st.subheader("🍵 You’re an oolong tea!")

        st.write("Unique, adventurous, and full of surprises.")

        oolong_image = Image.open("images2/oolong.jpeg")
        st.image(oolong_image, width = 180)
 
    else:

        st.subheader("⚡ You’re a black tea!")

        st.write("Strong, focused, and ready to take on anything.")

        blacktea_image = Image.open("images2/earlGrey.jpeg")
        st.image(blacktea_image, width = 180)

 
