import streamlit as st
import langchain_helper
st.title('Tourist place Generator ')
country_name = st.sidebar.selectbox("Select a country", ("India", "Malaysia", "Nepal", "Maldives"))

if country_name:
    response = langchain_helper.generate_state_name_and_tourist_places(country_name)
    st.header(f"State Name: {response['state_name'].strip()}")
    tourist_places = response['tourist_places'].strip().split(',')
    st.text('List of tourist places')
    st.write()
    for travel in tourist_places:
        st.write(' ', travel)





