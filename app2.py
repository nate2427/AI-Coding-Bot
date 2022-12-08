import streamlit as st
import requests

st.title('Users following #coding on Instagram') # this creates a title for our page
st.write('Here are all of the users who follow #coding on Instagram:') # this adds some text to our page

url = 'https://www.instagram.com/explore/tags/coding/' # sets up url variable which holds an API call URL
response = requests.get(url) # makes request using requests module to get data from instagram about users following hashtag "Coding"

print(response.text) # prints the response text to the console
# converts response object into json format so it can be accessed more easily
data = response.json() 
print(data)
# accesses json fields in order to find username values for each user who follows hashtag "Coding"
users = [user['username'] for user in data['graphql']['hashtag']['edge_hashtag_to_media']['edges'] ] 
for username in users:
    st.write(username) # adds each username from list onto Streamlit page