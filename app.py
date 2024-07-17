import streamlit as st

st.title("미래 시집 😂")

title=st.text_input("주제를 알려주세요!")

if st.button('시 짓기'):
    st.write(title)
    
