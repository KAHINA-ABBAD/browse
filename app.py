import pandas as pd
import streamlit as st
import requests


st.title('Taxi Fare Model ')

data_time = st.date_input('Date and time', value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
pickup_longitude = st.text_input('Pickup longitude')
pickup_latitude = st.text_input('Pickup latitude')
dropoff_longitude = st.text_input('Dropoff longitude')
dropoff_latitude = st.text_input('Dropoff latitude')
passenger_count = st.number_input('Passenger count', 1, 10)

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':



st.subheader('The parameters of my API.')
df = pd.DataFrame([{
          'Pickup longitude': pickup_longitude,
          'Pickup latitude': pickup_latitude,
          'Dropoff longitude': dropoff_longitude,
          'Dropoff latitude': dropoff_latitude,
          'Passenger count': passenger_count
        }])

df


st.subheader('Calling the API using the requests package')

result = requests.get(url).json()
result




st.subheader('The prediction from the **JSON** returned by the API')

'''

## Finally, we can display the prediction to the user
'''
