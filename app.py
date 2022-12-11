import streamlit as st
import requests

response = requests.get('https://p9function.azurewebsites.net/api/recommandation?user_id=600')

if response.status_code == 200:
    print("Succesful connection with API.")
    print('-------------------------------')
    data = response.json()
    print(data)
elif response.status_code == 404:
    print("Unable to reach URL.")
else:
    print("Unable to connect API or retrieve data.")

st.write(data)