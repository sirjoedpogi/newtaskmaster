import pandas as pd
import streamlit as st

# Load the task.csv file using pandas
df = pd.read_csv('task.csv')

# Set the title and description of the web app
st.set_page_config(page_title='PEDS TaskMaster', page_icon=':clipboard:', layout='wide')
st.write('# PEDS TaskMaster')
st.write('Task Management Web Application for PEDS')

# Show a selection box with 4 options
option = st.selectbox('Select an option', ('Show All Tasks', 'Your Tasks', 'Tasks you have Created', 'Create New Task'))

if option == 'Show All Tasks':
    # Show all tasks
    st.write(df)
    
elif option == 'Your Tasks':
    # Show tasks assigned to the current user
    current_user = st.text_input('Enter your username')
    df_user_tasks = df[df['task_doer'] == current_user]
    st.write(df_user_tasks)
    
elif option == 'Tasks you have Created':
    # Show tasks created by the current user
    current_user = st.text_input('Enter your username')
    df_user_created_tasks = df[df['task_maker'] == current_user]
    st.write(df_user_created_tasks)
    
elif option == 'Create New Task':
    # Allow the user to create a new task
    st.write('Create a new task')
    task_name = st.text_input('Task Name')
    task_project = st.text_input('Task Project')
    task_details = st.text_area('Task Details')
    task_maker = st.text_input('Task Maker')
    task_doer = st.text_input('Task Doer')
    task_start_date = st.date_input('Task Start Date')
    task_deadline = st.date_input('Task Deadline')
    task_time_left = (task_deadline - task_start_date).days * 24  # compute the time left in hours
    task_finished_proof = st.text_input('Task Finished Proof')
    task_priority = st.selectbox('Task Priority', ('High', 'Medium', 'Low'))
    task_status = 'on-going'
    new_task = pd.DataFrame({'task_id': [len(df)+1], 'task_name': [task_name], 'task_project': [task_project], 
                             'task_details': [task_details], 'task_maker': [task_maker], 'task_doer': [task_doer], 
                             'task_start_date': [task_start_date], 'task_deadline': [task_deadline], 
                             'task_time_left': [task_time_left], 'task_finished_proof': [task_finished_proof], 
                             'task_priority': [task_priority], 'task_status': [task_status]})
    df = pd.concat([df, new_task], ignore_index=True)
    st.write('New task created:', new_task)
    # Save the updated dataframe back to task.csv
    df.to_csv('task.csv', index=False)
