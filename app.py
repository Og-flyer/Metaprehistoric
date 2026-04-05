import streamlit as st
from stats import find_creature, loadDATA, locate_Answer, gameplay

st.title("Metaprehistoric")
guess = st.text_input("Write your guess:")

if st.button("Guess!"):
    result = find_creature(guess)
    if result:
        st.success("Found it!")
    else:
        st.error("Not found!")