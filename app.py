import streamlit as st
from bot import ask_ai_teacher_question
from streamlit_chat import message


# create a streamlit app
app = st
# set dark mode
app.set_page_config(page_title="AI Teacher", layout="wide", initial_sidebar_state="collapsed")

# create a title
app.title("AI Coding Bot")
# ask the user for a prompt
prompt = app.text_area(label="1", label_visibility="hidden", placeholder="Enter a prompt for the AI teacher")
# set up a question and answer list
if 'usr_msgs' not in app.session_state:
    app.session_state.usr_msgs = []
if 'bot_msgs' not in app.session_state:
    app.session_state.bot_msgs = []

if len(app.session_state.usr_msgs) > 0:
    for i in range(len(app.session_state.usr_msgs)):
        st.write(
            f"<div style='padding: 1rem; background-color: grey; color: white, border-radius: 0.5rem'> <p>Student: {app.session_state.usr_msgs[i]}</p></div>",unsafe_allow_html=True)
        st.write("<div style='padding: 1rem; background-color: black; color: white, border-radius: 0.5rem; margin-top: 1rem'> Teacher: " + app.session_state.bot_msgs[i]+ "</p></div>",unsafe_allow_html=True)
       


            
placeholder = st.empty() # placeholder for latest message
input_ = st.text_input(label ="2", label_visibility="hidden",placeholder="Speak")
# create a button to send the message
if st.button("Send"):
    if input_ and prompt:
        # get the latest message
        latest_message = input_
        usr_last_6_msgs = []
        bot_last_6_msgs = []
        if len(app.session_state.usr_msgs) > 6:
            usr_last_6_msgs = app.session_state.usr_msgs[-6:]
            bot_last_6_msgs = app.session_state.bot_msgs[-6:]
        else:
            usr_last_6_msgs = app.session_state.usr_msgs
            bot_last_6_msgs = app.session_state.bot_msgs
        # get the bot's response
        bot_response = ask_ai_teacher_question(prompt, latest_message, usr_last_6_msgs[::-1], bot_last_6_msgs[::-1])
        # add the message to the list of messages
        app.session_state.usr_msgs.append(latest_message)
        # add the bot's response to the list of messages
        app.session_state.bot_msgs.append(bot_response)
        # clear the input field
        input_ = ""
        st.experimental_rerun()
    # if no prompt is given, show an error message
    if not prompt:
        st.error("Please enter a prompt for the AI teacher")
    # if no message is given, show an error message
    if not input_:
        st.error("Please enter a message")

# with placeholder.container():
#     if len(st.session_state.usr_msgs) > 0:
#         message( st.session_state.usr_msgs[-1], is_user=True) # display the latest message

