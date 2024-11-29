import streamlit as st
import datetime
import requests
import pandas as pd

st.markdown(''' # Estimate your taxi fare! 🚕💰''')
st.markdown(''' ## Please enter the following information regarding your next ride:''')

def get_input():
    input_items = {
    'pickup time': st.date_input('Enter the pickup time: ', datetime.date(2019, 7, 6)),
    'pickup longitude': st.number_input('Enter the pickup longitude: '),
    'pickup latitude': st.number_input('Enter the pickup latitude: '),
    'dropoff longitude': st.number_input('Enter the dropoff longitude: '),
    'dropoff latitude': st.number_input('Enter the dropoff latitude: '),
    'passenger count': st.number_input('Enter the passenger count: ')
    }
    time, pickup_longitude,pickup_latitude,dropoff_longitude, dropoff_latitude, passengers  = input_items.values()

    st.write('Your ride details are: Time: ', time , 'Pickup Longitude: ', pickup_longitude, 'Pickup Latitude: ', pickup_latitude, 'Dropoff Longitude: ', dropoff_longitude, 'Dropoff Latitude: ', dropoff_latitude, 'Passenger Count: ', passengers)
    return print(input_items)

ride_info = get_input()

print(ride_info)


url = 'https://taxifare.lewagon.ai/predict'
pred = requests.get(url, ride_info).json()
final_pred = pred

st.markdown(f'This ride will cost you: ${final_pred}')
