import streamlit as st
import datetime
import requests

st.set_page_config(
    page_title="Practice What You Preach",
    page_icon=":material/edit:",
    layout='wide'
    )

'''
# Practice What You Preach
'''



# Initialize session state for managing views if not already set
if 'current_view' not in st.session_state:
    st.session_state.current_view = "menu"

st.header("Select an Option")

st.write("Default time period is the current government cycle")

col1, col2 = st.columns(2)

today = datetime.datetime.now()
last_year = today.year - 1

with col1:
    start_date = st.date_input("When's your birthday", datetime.date(2025, 2, 23))

with col2:
    end_date = st.date_input("When's your birthday", datetime.date(today.year,today.month,today.day))

############################################################################
st.divider()

col3, col4 = st.columns(2)

with col3:
    st.text_area("Party Summary",
                 "The party advocates for regulated migration pathways through visa agreements and training partnerships for students, trainees, and skilled workers. They believe in human rights-based cooperation with third and transit countries, emphasizing that more regulated migration leads to less irregular migration. The goal is to effectively and long-term reduce irregular and dangerous migration to Europe by creating better local living conditions and implementing comprehensive migration agreements. They explicitly oppose outsourcing asylum procedures to third countries, citing cost and legal failures. The party also stresses the importance of distinguishing between flight and labor migration.",
                 height=250
                 )

###########################################################################

url = 'INSERT API URL HERE'

params = {
    'start_date': start_date,
    'end_date': end_date,

}

# response = requests.get(url, params=params).json()
# fare = response['fare']
