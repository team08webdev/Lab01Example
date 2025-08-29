import streamlit as st
 
st.title("✨ What Type of Coffee Are You? ☕")
 
st.write("Answer the questions below to find out what coffee matches your personality!")
 
# Question 1

q1 = st.radio(

    "How do you usually spend your weekend?",

    ("Relaxing with a book", "Hanging out with friends", "Exploring new places", "Catching up on work")

)
 
# Question 2

q2 = st.radio(

    "Pick a vacation destination:",

    ("Paris", "Tokyo", "New York", "Bali")

)
 
# Question 3

q3 = st.radio(

    "What’s your go-to vibe?",

    ("Calm and cozy", "Fun and energetic", "Adventurous", "Focused and productive")

)
 
# Simple result logic (without lists/dicts/session_state)

if st.button("Show My Coffee Personality!"):

    if q1 == "Relaxing with a book" or q3 == "Calm and cozy":

        st.subheader("☕ You’re a Latte!")

        st.write("Warm, comforting, and always reliable.")

        st.balloons()
 
    elif q1 == "Hanging out with friends" or q3 == "Fun and energetic":

        st.subheader("🥤 You’re an Iced Coffee!")

        st.write("Cool, refreshing, and always a good time.")
 
    elif q1 == "Exploring new places" or q2 == "Tokyo":

        st.subheader("🍵 You’re a Matcha Latte!")

        st.write("Unique, adventurous, and full of surprises.")
 
    else:

        st.subheader("⚡ You’re an Espresso!")

        st.write("Strong, focused, and ready to take on anything.")

 
