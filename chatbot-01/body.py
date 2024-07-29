import streamlit as st
# from storage import Storage (optional) and also enable line 17 below
from brain import chatbot_brain


name = "i B🤖t" # name your chatbot here

st.markdown(f"<h1>{name}</h1>",
            unsafe_allow_html=True)

# Form
with st.form(key="my_form"):
    user_question = st.text_input("Enter Your Question")
    submit_btn = st.form_submit_button(label="submit question")

if submit_btn:
    
    st.write(user_question) # testing to see your input displayed after the submit button is clicked

    # enable this and disable line 18, to get actual answer from gpt-3
    
    # response = chatbot_brain(user_question)
    # st.write(f"response from the brain : {response}")