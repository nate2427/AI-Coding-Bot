import streamlit as st
from bot import ask_ai_teacher_question
from streamlit_ace import st_ace

# create a streamlit app
app = st
lang_opts = ["Python", "Javascript"]
# turn all the options to lowercase
lang_opts = [lang.lower() for lang in lang_opts]
# set dark mode
app.set_page_config(page_title="AI Teacher", layout="wide", initial_sidebar_state="collapsed")

# create a title
app.title("AI Coding Bot")
# ask the user for a prompt
# prompt = app.text_area(label="1", label_visibility="hidden", placeholder="Enter a prompt for the AI teacher")

col1, col2 = app.columns(2)
# set up a question and answer list
if 'usr_msgs' not in app.session_state:
    app.session_state.usr_msgs = []
if 'bot_msgs' not in app.session_state:
    app.session_state.bot_msgs = []

slctd_lang_opt=None
placeholder = col1.empty() # placeholder for latest message
input_ = col1.text_area(label ="2", label_visibility="hidden",placeholder="How can I help you?")
code = None
with col2:
    slctd_lang_opt = st.selectbox("Select a language", label_visibility='hidden', options=lang_opts)
    code = st_ace(language=slctd_lang_opt, theme='tomorrow_night_eighties', min_lines=25)
    st.subheader("Code Output")
    st.markdown("``` {}\n".format(slctd_lang_opt) + code + "\n```")
 
# create a button to send the message
if col1.button("Send"):
    prompt = "You are the best at showing new coders how to code complicated {} projects. Explain to your human companion through code examples, in a conversational fashion, how to code the project he is working on. Make sure to show code examples and to explain the code and the logic behind it so that a second grader can understand it.".format(slctd_lang_opt)
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


if len(app.session_state.usr_msgs) > 0:
    for i in range(len(app.session_state.usr_msgs)-1, -1, -1):
        col1.write("<div style='padding: 1rem; background-color: black; color: white; border-radius: 0.5rem; margin-top: 1rem; margin-bottom: 1rem'> Teacher: " + app.session_state.bot_msgs[i]+ "</p></div>",unsafe_allow_html=True)
        col1.write(
            f"<div style='padding: 1rem; background-color: lightblue; color: black; border-radius: 0.5rem'> <p>Student: {app.session_state.usr_msgs[i]}</p></div>",unsafe_allow_html=True)
