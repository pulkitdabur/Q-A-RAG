import streamlit as st
from app import *

def main():
    st.title("Q & A for budget 2025")
    st.write("Enter your question related to the document to get specific information")

    if 'user_question' not in st.session_state:
        st.session_state.user_question=""

    if 'answer' not in st.session_state:
        st.session_state.aswer= None

    user_question = st.text_input("Enter Your question:", value = st.session_state.user_question)

    if st.button('Search'):
        if user_question:
            try:
                answer=main_func(user_question)
                st.session_state.answer = answer
                st.success("Answer Found")
                st.write(answer)
            except Exception as e:
                st.error(f"Error processing your question: {str(e)}")
        else:
            st.error("Please enter a question to search")

    if st.button("Reset"):
        st.session_state.user_question=""
        st.session_state.asnwer= None
        st.rerun()

if __name__=="__main__":
    main()