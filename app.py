import streamlit as st
import datetime

st.markdown(''' # Estimate your taxi fare! 🚕💰''')

def get_input():
    st.write('please enter the following information regarding your next ride:')
    input_items = {
    'pickup time': st.date_input('Enter the pickup time: ', datetime.date(2019, 7, 6)),
    'pickup longitude': st.number_input('Enter the pickup longitude: '),
    'pickup latitude': st.number_input('Enter the pickup latitude: '),
    'dropoff longitude': st.number_input('Enter the dropoff longitude: '),
    'dropoff latitude': st.number_input('Enter the dropoff latitude: '),
    'passenger count': st.number_input('Enter the passenger count: ')
    }
    st.write('Your ride details are: ', input_items.items())
    return input_items
get_input()


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
