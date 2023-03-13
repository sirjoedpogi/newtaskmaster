import pandas as pd
import streamlit as st
import datetime
from PIL import Image

# Load the task.csv file using pandas
df_tasks = pd.read_csv('task.csv')
df_users = pd.read_csv('users.csv')

# Set the title and description of the web app

##st.set_page_config(page_title='PEDS TaskMaster', page_icon=':clipboard:', layout='wide')
##st.write('# PEDS TaskMaster')
##st.write('Task Management Web Application for PEDS')
##logo_image = r"C:\Users\CSPC\Desktop\newtaskmaster\logo peds.png"
##st.image(logo_image, width=200)

st.set_page_config(page_title='PEDS TaskMaster', page_icon=':clipboard:', layout='wide')
st.write('# PEDS TaskMaster')
st.write('Task Management Web Application for PEDS')

# Load the image
logo_image = Image.open("logo peds.png")

# Display the image using Streamlit
st.image(logo_image, width=200)

# Show a selection box with 4 options
option = st.selectbox('Select an option', ('Show All Unfinished Tasks', 'Show All Finished Tasks','Show all Task that Missed Deadline','Your Tasks', 'Tasks you have Created', 'Create New Task'))

if option in ('Your Tasks', 'Tasks you have Created', 'Create New Task'):
    username = st.text_input('Enter your username')
    password = st.text_input('Enter your password', type='password')
    
    # Check whether the input username and password match with any record in the users.csv file
    if not ((df_users['username'] == username) & (df_users['password'] == password)).any():
        st.error('Incorrect username or password. Please try again.')
        st.stop()

if option == 'Show All Unfinished Tasks':
    # Show all unfinished tasks
    df_all_unfinished_tasks = df_tasks.loc[(df_tasks['task_status'].isin(['on-going', 'proof-sent']))]
    st.write(df_all_unfinished_tasks)

elif option == 'Show All Finished Tasks':
    # Show all unfinished tasks
    df_all_finished_tasks = df_tasks.loc[(df_tasks['task_status'].isin(['accomplished']))]
    st.write(df_all_finished_tasks)

elif option == 'Show all Task that Missed Deadline':
    # Show all unfinished tasks
    df_all_task_missed_deadline = df_tasks.loc[(df_tasks['task_status'].isin(['missed-deadline']))]
    st.write(df_all_task_missed_deadline)
    


##elif option == 'Your Tasks':
##    st.write('ALL ON-GOING AND PROOF -SENT TASKS')
##
##        
##    # Show tasks assigned to the current user
##    #df_user_tasks = df_tasks[df_tasks['task_doer'] == username]  & (df_tasks['task_status'].isin(['on-going', 'proof-sent']))
##    df_user_tasks = df_tasks.loc[(df_tasks['task_doer'] == username) & (df_tasks['task_status'].isin(['on-going', 'proof-sent']))]
##    if st.button("Show/Refresh Data"):
##        df_tasks = pd.read_csv('task.csv')
##        st.write(df_user_tasks)
##    # Show the user's tasks with the updated task_finished_proof column
##    ##st.write(df_user_tasks)
##    st.write('___')
##
##    # Add a text input box for the user to enter a URL
##    st.write("Upload URL of Proof of Finished Task:")
##    url_input = st.text_input("Enter URL here:")
##
##
##    # Add a button to upload the URL to the "task_finished_proof" column for the selected task
##    for index, row in df_user_tasks.iterrows():
##        if st.button(f"Upload URL Proof for Task {index+1}"):
##            df_tasks.loc[index, 'task_finished_proof'] = url_input
##            df_tasks.loc[index, 'task_status'] = 'proof-sent'
##            df_tasks.loc[index, 'task_proof_date'] = datetime.datetime.now()
##            st.write(f"URL uploaded for Task {index+1} successfully.")
##            df_tasks.to_csv('task.csv', index=False)
##            # Update the displayed task status
##            st.write(f"Task {index+1}: {row['task_name']}")
##            st.write(f"Task Status: proof-sent")
##    st.write('___')
##    
##    st.write('ALL ACCOMPLISHED TASKS')
##    df_user_accomplished_tasks = df_tasks.loc[(df_tasks['task_doer'] == username) & (df_tasks['task_status'].isin(['accomplished']))]
##    st.write(df_user_accomplished_tasks)

elif option == 'Your Tasks':
    st.write('ALL ON-GOING AND PROOF -SENT TASKS')

    # Show tasks assigned to the current user
    df_user_tasks = df_tasks.loc[(df_tasks['task_doer'] == username) & (df_tasks['task_status'].isin(['on-going', 'proof-sent']))]
    if st.button("Show/Refresh Data"):
        df_user_tasks = df_tasks.loc[(df_tasks['task_doer'] == username) & (df_tasks['task_status'].isin(['on-going', 'proof-sent']))]
        df_tasks = pd.read_csv('task.csv')
    st.write(df_user_tasks)
        
    
    # Create a selection box to select a task to upload proof for
    task_options = ['Select a task'] + list(df_user_tasks['task_name'])
    selected_task = st.selectbox("Select a task to for proof uploading", task_options)

    # Add a text input box for the user to enter a URL
    st.write("Upload URL of Proof of Finished Task:")
    url_input = st.text_input("Enter URL here:")

    # Add a button to upload the URL to the "task_finished_proof" column for the selected task
    if st.button("Upload URL Proof"):
        if selected_task == 'Select a task':
            st.warning("Please select a task first.")
        else:
            index = df_user_tasks[df_user_tasks['task_name'] == selected_task].index[0]
            df_tasks.loc[index, 'task_finished_proof'] = url_input
            df_tasks.loc[index, 'task_status'] = 'proof-sent'
            df_tasks.loc[index, 'task_proof_date'] = datetime.datetime.now()
            st.write(f"URL uploaded for Task {selected_task} successfully.")
            df_tasks.to_csv('task.csv', index=False)
            
    st.write('___')

    st.write('ALL ACCOMPLISHED TASKS')
    
    df_user_finishedtasks = df_tasks.loc[(df_tasks['task_doer'] == username) & (df_tasks['task_status'].isin(['accomplished']))]
    if st.button("Show/Refresh Data", key="refresh_button"):
        df_tasks = pd.read_csv('task.csv')
        df_user_finishedtasks = df_tasks.loc[(df_tasks['task_doer'] == username) & (df_tasks['task_status'].isin(['accomplished']))]
    st.write(df_user_finishedtasks)


    
    

    
##elif option == 'Tasks you have Created':
##    # Show tasks created by the current user
##
##    df_user_created_tasks = df_tasks[df_tasks['task_maker'] == username]
##    st.write(df_user_created_tasks)


##

elif option == 'Tasks you have Created':
    # Show tasks created by the current user

    
    df_user_created_tasks = df_tasks.loc[(df_tasks['task_maker'] == username) & (df_tasks['task_status'].isin(['on-going', 'proof-sent']))]
    if st.button("Show/Refresh Data", key="refresh_task_created_button"):
        df_tasks = pd.read_csv('task.csv')
        df_user_created_tasks = df_tasks.loc[(df_tasks['task_maker'] == username) & (df_tasks['task_status'].isin(['on-going', 'proof-sent']))]
    st.write(df_user_created_tasks)

    # Find the tasks with status "proof-sent"
    df_proof_sent_tasks = df_user_created_tasks[df_user_created_tasks['task_status'] == 'proof-sent']
    

    # Display URLs for proof-sent tasks and add a button to confirm finished task
    for index, row in df_proof_sent_tasks.iterrows():
        st.write(f"Task {index + 1}: {row['task_name']}")
        st.write(f"URL for finished task proof: {row['task_finished_proof']}")

        if st.button(f"Confirm finished task for Task {index + 1}"):
            df_tasks.loc[index, 'task_status'] = 'accomplished'
            df_tasks.loc[index, 'task_accomp_date'] = datetime.datetime.now()
            st.write(f"Task {index + 1} status changed to accomplished.")
            df_tasks.to_csv('task.csv', index=False)

    # If no proof-sent tasks found, display message
    if len(df_proof_sent_tasks) == 0:
        st.write("You currently have no tasks with status 'proof-sent'.")



##elif option == 'Create New Task':
##
##    
##    users_list = df_users["username"].tolist()
##
##    if username in users_list:
##        users_list.remove(username)
##
##    # Create a selection box with the list of users
##   
##
##
##    # Allow the user to create a new task
##    st.write('Create a new task')
##    task_name = st.text_input('Task Name')
##    task_project = st.text_input('Task Project')
##    task_details = st.text_area('Task Details')
##    task_maker = username
##    task_doer = st.selectbox('Task Doer', users_list)
##    task_start_date = st.date_input('Task Start Date')
##    task_deadline = st.date_input('Task Deadline')
##    task_time_left = (task_deadline - task_start_date).days * 24  # compute the time left in hours
##    task_priority = st.selectbox('Task Priority', ('High', 'Medium', 'Low'))
##    task_status = 'on-going'
##
##    
##    new_task = pd.DataFrame({'task_id': [len(df_tasks)+1], 'task_name': [task_name], 'task_project': [task_project], 
##                             'task_details': [task_details], 'task_maker': [task_maker], 'task_doer': [task_doer], 
##                             'task_start_date': [task_start_date], 'task_deadline': [task_deadline], 
##                             'task_time_left': [task_time_left],  'task_priority': [task_priority], 'task_status': [task_status]})
##    if st.button('Submit'):
##        df_tasks = pd.concat([df_tasks, new_task], ignore_index=True)
##        st.write('New task created:', new_task)
##        # Save the updated dataframe back to task.csv
##        df_tasks.to_csv('task.csv', index=False)


elif option == 'Create New Task':

    
    users_list = df_users["username"].tolist()

    if username in users_list:
        users_list.remove(username)

    # Create a selection box with the list of users
   


    # Allow the user to create a new task
    st.write('Create a new task')
    task_name = st.text_input('Task Name')
    task_project = st.text_input('Task Project')
    task_details = st.text_area('Task Details')
    task_maker = username
    task_doer = st.selectbox('Task Doer', users_list)
    task_start_date = datetime.datetime.now() # get current time
    task_deadline_date = st.date_input('Task Deadline Date')
    task_deadline_time = st.time_input('Task Deadline Time')
    task_deadline = datetime.datetime.combine(task_deadline_date, task_deadline_time)
    task_time_left = (task_deadline - task_start_date).days * 24  # compute the time left in hours
    task_priority = st.selectbox('Task Priority', ('High', 'Medium', 'Low'))
    task_status = 'on-going'

    
    new_task = pd.DataFrame({'task_id': [len(df_tasks)+1], 'task_name': [task_name], 'task_project': [task_project], 
                             'task_details': [task_details], 'task_maker': [task_maker], 'task_doer': [task_doer], 
                             'task_start_date': [task_start_date], 'task_deadline': [task_deadline], 
                             'task_time_left': [task_time_left],  'task_priority': [task_priority], 'task_status': [task_status]})
    if st.button('Submit'):
        df_tasks = pd.concat([df_tasks, new_task], ignore_index=True)
        st.write('New task created:', new_task)
        # Save the updated dataframe back to task.csv
        df_tasks.to_csv('task.csv', index=False)
