import openai
from dotenv import load_dotenv
load_dotenv()
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def create_ques_anws_str(usr_msgs, bot_msgs):
    ques_anws_str = ""
    for i in range(len(usr_msgs)):
        ques_anws_str += f"student: {usr_msgs[i]}\nteacher: {bot_msgs[i]}\n"
    return ques_anws_str

def ask_ai_teacher_question(prompt, cur_question, usr_msgs, bot_msgs):
    ques_anws_str = create_ques_anws_str(usr_msgs, bot_msgs)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt + f"\n{ques_anws_str}\nstudent: {cur_question}\nteacher: ",
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.72,
        presence_penalty=0
    )
    return str(response.choices[0].text)