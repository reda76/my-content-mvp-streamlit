import streamlit as st
import requests


st.header("Recommandation d'article")
st.write("Vous pouvez choisir ici un id d'utilisateur, 5 id d'articles seront alors recommandés")

option = st.selectbox("Vous pouvez choisir ici un id d'utilisateur, 5 id d'articles seront alors recommandés",
   (5, 10, 15, 20, 25, 30, 35))

st.write('You selected:', option)
if option:
    response = requests.get('https://p9fonction.azurewebsites.net/api/recommandation?user_id='+str(option))

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