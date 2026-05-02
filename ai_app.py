import streamlit as st

st.title("ljus")

savol = st.text_input("kimsan:")

if savol:
    javob = f"Savoling: {savol}. Men hali o‘rganayapman 😄"
    st.write(javob)