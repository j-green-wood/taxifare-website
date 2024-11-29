import streamlit as st
import datetime
import requests
import pandas as pd

st.markdown(''' # Estimate your taxi fare! 🚕💰''')
st.markdown(''' Please enter the following information regarding your next ride:''')


pickup_time = st.date_input('Enter the pickup time: '),
pickup_longitude = st.number_input('Enter the pickup longitude: '),
pickup_latitude = st.number_input('Enter the pickup latitude: '),
dropoff_longitude = st.number_input('Enter the dropoff longitude: '),
dropoff_latitude = st.number_input('Enter the dropoff latitude: '),
passenger_count = st.number_input('Enter the passenger count: ')

st.write('Your ride details are: Time: ', pickup_time , 'Pickup Longitude: ', pickup_longitude, 'Pickup Latitude: ', pickup_latitude, 'Dropoff Longitude: ', dropoff_longitude, 'Dropoff Latitude: ', dropoff_latitude, 'Passenger Count: ', passengers)

ride_info = {
    'pickup_datetime': pickup_time,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

url = 'https://taxifare.lewagon.ai/predict'
pred = requests.get(url, ride_info).json()
final_pred = pred

st.markdown(f'This ride will cost you: ${final_pred}')
