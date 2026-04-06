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
    Daily_chosen_DATA = Daily_chosen
    if "won" not in st.session_state:
        st.session_state.won = False
    if "guesses" not in st.session_state:
        st.session_state.guesses = []
    if not st.session_state.won:
        guess = st_searchbox(search_creatures, placeholder="Write your guess: ")
        if st.button("Guess!"):
            if guess is None:
                st.stop()
            already_guessed = [r.get("guess_name") for r in st.session_state.guesses]
            if guess in already_guessed:
                st.warning("You already guessed that!")
                st.stop()
            guess_DATA = find_creature(guess)
            if guess_DATA is None:
                st.error("Creature not found!")
                st.stop()
            if guess_DATA["name"] == Daily_chosen_DATA["name"]:
                st.session_state.won = True
                st.rerun()
            else:
                st.error("Wrong!")
                result = {}
                Last_Match = None
                for i in Daily_chosen_DATA:
                    if i == "name":
                        continue
                    elif guess_DATA[i]["value"] == Daily_chosen_DATA[i]["value"]:
                         result[i] = (Daily_chosen[i]["value"], Daily_chosen[i]["wiki"])
                         Last_Match = i
                result["guess_name"] = guess
                result["last_match"] = Last_Match
                st.session_state.guesses.append(result)        
    else:
        st.session_state.guesses = []
        st.success(f"Correct! The answer was {Daily_chosen_DATA['name']}")
        for i in Daily_chosen_DATA:
                if i == "name":
                    continue
                st.write(f"{i}: {Daily_chosen_DATA[i]['value']}")
        st.markdown(Daily_chosen_DATA["species"]["wiki"])
    
    for result in st.session_state.guesses:
        Last_Match = result.get("last_match")
        for key, val in result.items():
            if key == "last_match":
                continue
            if key == "guess_name":
                continue
            value, wiki = val
            st.write(f"{key}: {value}")
        if Last_Match:
            st.markdown(f"[{Daily_chosen[Last_Match]['value']}]({Daily_chosen[Last_Match]['wiki']})")
        st.divider()
    
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
