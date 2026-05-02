import streamlit as st
import random 
st.title("Rock Paper Scissor GAME")
st.subheader("Created by adithii")
st.write("You will be playing rock paper scisscor with the computer.Enter your choice in the box and may the best win!")
title = st.text_input(label="Enter Input",value= "Rock, Paper, scissors")
a=random.choice(["rock","paper","scissors"])

if st.button("go"):
    if title==a:
        st.info("It's draw! ")
    else : 
        if title=="rock" and a=="scissors" : 
            st.success("you won!")
            st.balloon()
        elif title=="scissors" and a=="paper" :
            st.success("You won!")
            st.balloon()
        elif title=="paper" and a=="rock" :
            st.success("you won!")
            st.balloon()
        else :
            st.warning("You lose!")
            st.snow()
    st.write("You have put "+ str(title))
    st.write(" the computer has put "+ str(a))
