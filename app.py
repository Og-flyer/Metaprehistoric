import streamlit as st
from stats import find_creature, loadDATA, locate_Answer, gameplay
from streamlit_searchbox import st_searchbox

def search_creatures(query):
    creatures = loadDATA()
    results = []
    names = [c["name"] for c in creatures]
    for name in names:
        if query.lower() in name.lower():
            results.append(name)
    return results

st.title("Metaprehistoric")
guess = st_searchbox(search_creatures, placeholder="Write your guess: ")

if "daily" not in st.session_state:
    st.session_state.daily = locate_Answer()
Daily_chosen = st.session_state.daily 

if st.button("Guess!"):
    Daily_chosen_DATA = Daily_chosen
    guess_DATA = find_creature(guess)
    if guess_DATA is None:
        st.error("Creature not found!")
        st.stop()
    if guess_DATA["name"] == Daily_chosen_DATA["name"]:
        st.success(f"Correct! The answer was {Daily_chosen_DATA['name']}")
        for i in Daily_chosen_DATA:
            st.write(f"{i}: {Daily_chosen_DATA[i]}")
    else:
        st.error("Wrong!")
        for i in Daily_chosen_DATA:
            if i == "name":
                continue
            elif guess_DATA[i] == Daily_chosen_DATA[i]:
                st.write(f"{i}: {Daily_chosen_DATA[i]}")
