import streamlit as st
from bot import ask_ai_teacher_question
from streamlit_chat import message


# create a streamlit app
app = st

# create a title
app.title("AI Coding Bot")
# ask the user for a prompt
prompt = app.text_area("Enter a prompt for the AI teacher")
# set up a question and answer list
if 'usr_msgs' not in app.session_state:
    app.session_state.usr_msgs = []
if 'bot_msgs' not in app.session_state:
    app.session_state.bot_msgs = []

if len(app.session_state.usr_msgs) > 0:
    for i in range(len(app.session_state.usr_msgs)):
        st.markdown(f"**Student:** {app.session_state.usr_msgs[i]}")
        st.markdown(f"**Teacher:** {app.session_state.bot_msgs[i]}")
       


            
placeholder = st.empty() # placeholder for latest message
input_ = st.text_input("you: ")
# create a button to send the message
if st.button("Send"):
    if input_ and prompt:
        # get the latest message
        latest_message = input_
        # add the message to the list of messages
        app.session_state.usr_msgs.append(latest_message)
        # get the bot's response
        # bot_response = ask_ai_teacher_question(prompt, latest_message, app.session_state.usr_msgs, app.session_state.bot_msgs)
        bot_response = 'what up doe'
        # add the bot's response to the list of messages
        app.session_state.bot_msgs.append(bot_response)
        # clear the input field
        input_ = ""
        # update the placeholder with the latest message
        # placeholder.text(f"**Student:** {latest_message}")
        # placeholder.text(f"**Teacher:** {bot_response}")
        # scroll to the bottom of the page
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