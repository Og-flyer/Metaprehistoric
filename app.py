import streamlit as st
from stats import find_creature, loadDATA, locate_Answer
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

def game(Daily_chosen):
    guess = st_searchbox(search_creatures, placeholder="Write your guess: ")
    if st.button("Guess!"):
        if guess is None:
            st.stop()
        Daily_chosen_DATA = Daily_chosen
        guess_DATA = find_creature(guess)
        if guess_DATA is None:
            st.error("Creature not found!")
            st.stop()
        if guess_DATA["name"] == Daily_chosen_DATA["name"]:
            st.success(f"Correct! The answer was {Daily_chosen_DATA['name']}")
            for i in Daily_chosen_DATA:
                if i == "name":
                    continue
                st.write(f"{i}: {Daily_chosen_DATA[i]['value']}")
            st.markdown(Daily_chosen_DATA["species"]["wiki"])
        else:
            st.error("Wrong!")
            Last_Match = None
            for i in Daily_chosen_DATA:
                if i == "name":
                    continue
                elif guess_DATA[i]["value"] == Daily_chosen_DATA[i]["value"]:
                    st.write(f"{i}: {Daily_chosen_DATA[i]['value']}")
                    Last_Match = i
            st.markdown(Daily_chosen_DATA[Last_Match]["wiki"])
    return None

def Practice():
    if "daily" not in st.session_state:
        st.session_state.daily = locate_Answer()
    Daily_chosen = st.session_state.daily 
    game(Daily_chosen)
    return None

def Daily():
    return None

if "mode" not in st.session_state:
    st.write("Choose a mode:")
    col1, col2 = st.columns(2)
    if col1.button("Daily Challenge Mode"):
        st.session_state.mode = "daily"
        st.rerun()
    if col2.button("Practice Mode"):
        st.session_state.mode = "practice"
        st.rerun()
else:
    if st.session_state.mode == "daily":
        Daily()
    elif st.session_state.mode == "practice":
        Practice()
