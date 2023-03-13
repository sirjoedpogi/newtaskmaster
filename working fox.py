import pandas as pd
import streamlit as st

# Load the users.csv file into a pandas DataFrame
users_df = pd.read_csv("users.csv")

# Define a function to check if a given username and password are valid
def authenticate(username, password):
    # Check if the username and password match any entries in the users.csv file
    valid_user = users_df[(users_df["username"] == username) & (users_df["password"] == password)]
    return not valid_user.empty

# Define a function to filter the task DataFrame by task doer or task maker
def filter_tasks(username, task_df, task_type):
    if task_type == "Your Tasks":
        # Filter tasks where the task_doer column matches the given username
        filtered_df = task_df[task_df["task_doer"] == username]
    elif task_type == "Tasks you have Created":
        # Filter tasks where the task_maker column matches the given username
        filtered_df = task_df[task_df["task_maker"] == username]
    else:
        # Return the full task DataFrame if creating a new task
        filtered_df = task_df
    return filtered_df

# Define a function to show the filtered task DataFrame
def show_tasks(filtered_df):
    # Show the task details in a table
    st.write(filtered_df)

# Define a function to prompt the user for their username and password
def login():
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    return username, password

# Load the task.csv file into a pandas DataFrame
task_df = pd.read_csv("task.csv")

# Define the options for the selection box
options = ["Show All Tasks", "Your Tasks", "Tasks you have Created", "Create New Task"]

# Show the selection box
option = st.sidebar.selectbox("Select an option:", options)

# If the user selects "Your Tasks" or "Tasks you have Created", prompt for their username and password
if option in ["Your Tasks", "Tasks you have Created"]:
    username, password = login()
    # If the username and password are valid, filter the task DataFrame and show the results
    if authenticate(username, password):
        filtered_df = filter_tasks(username, task_df, option)
        show_tasks(filtered_df)
    # If the username and password are not valid, show an error message
    else:
        st.error("Invalid username or password. Please try again.")
# If the user selects "Show All Tasks" or "Create New Task", show the task DataFrame without filtering
else:
    show_tasks(task_df)
