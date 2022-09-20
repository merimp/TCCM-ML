import streamlit as st

st.title("This is my first app")

my_text = st.text("A random version 2 of text")

my_button = st.button("Run ML computation")

if my_button:
	st.title("The model is running...")

my_text_2 = st.text("Hola")
