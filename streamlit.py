import streamlit as st
import pandas as pd
import requests

url = "http://openapi.seoul.go.kr:8088/6c75517a567468753131364874457863/json/SeoulLibNewArrivalInfo/1/5/"
response = requests.get(url)
data = response.json()["SeoulLibNewArrivalInfo"]["row"]

df = pd.DataFrame(data)

search_query = st.text_input("Search by title")

if search_query:
    df = df.query(f"TITLE.str.contains('{search_query}')")

st.table(df)
