import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my ToDo App")
st.write("This app is used to increase Productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new ToDo", key="new_todo", on_change=add_todo)
