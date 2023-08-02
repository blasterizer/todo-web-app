import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is my ToDo App")
st.write("This app is used to increaes Productivity")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new ToDo")
