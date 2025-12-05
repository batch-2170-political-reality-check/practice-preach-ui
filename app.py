from datetime import date, datetime
import streamlit as st
import requests
from constants import BUNDESTAG_WAHLPERIODE
# from pages import page_1,page_2

#################################### Page Configs   #########################################
st.set_page_config(
    page_title="Practice What You Preach",
    page_icon="🦔",
    layout='wide'
    )

# Reducing the margins at the top so
st.markdown("""
<style>
header.stAppHeader {
    background-color: transparent;
}
section.stMain .block-container {
    padding-top: 0rem;
    z-index: 1;
}
</style>""", unsafe_allow_html=True)


# ################################# API Call ##########################################

url = 'https://rag-service-27wbaw4ioq-oe.a.run.app/parameters'

# params = {
#     'start_date': start_date,
#     'end_date': end_date,
#     'topic': topic,
#     'party': party

# }

response = requests.get(url).json()


topic = list(response['political_topics'].keys())
for i in range(len(topic)):
    topic[i] = topic[i].replace('_',' ')
    if ' ' in topic[i]:
        g = topic[i].split(' ')
        for h in range(len(g)):
            g[h] = g[h].capitalize()
        topic[i] = ' '.join(g)
    else:
        topic[i] = topic[i].capitalize()


topics = sorted(topic)

#################################### Topic Navigation #########################################

# topics = ["Climate","Digital","Mett Igel","Lederhosen","Bier","Deutsch Rap","Berlin","Ballern","Skifahrt","ß"]

pages = [
        st.Page("home.py", title="Home"),
        st.Page("page_1.py", title=topics[0]),
        st.Page("page_2.py", title= topics[1]),
        st.Page("page_3.py", title= topics[2]),
        st.Page("page_4.py", title= topics[3]),
        st.Page("page_5.py", title= topics[4]),
        st.Page("page_6.py", title= topics[5]),
        st.Page("page_7.py", title= topics[6]),
        st.Page("page_8.py", title= topics[7]),
        st.Page("page_9.py", title= topics[8]),
        st.Page("page_10.py", title= topics[9]),
    ]

# pages = [
#         st.Page("app.py", title="Home"),
#         st.Page(page_1, title=topics[0]),
#         st.Page(page_2, title= topics[1]),
#         st.Page(page_3.py, title= topics[2]),
#         st.Page(page_4.py, title= topics[3]),
#         st.Page(page_5.py, title= topics[4]),
#         st.Page(page_6.py, title= topics[5]),
#         st.Page(page_7.py, title= topics[6]),
#         st.Page(page_8.py, title= topics[7]),
#         st.Page(page_9.py, title= topics[8]),
#         st.Page(page_10.py, title= topics[9]),
#     ]

# pg = st.navigation(pages, position='sidebar')
# pg.run()

# pages = [
#         st.Page("page_1.py", title="Create your account"),
#         st.Page("page_2.py", title="Learn about us")
#     ]


pg = st.navigation(pages)
pg.run()



################################### Sidebar Dates ##########################################
st.divider()

st.sidebar.write("Choose a time period within Wahlperiode dates.")

bundestag_periods = response['bundestag_wahlperiode']

def string_to_date(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d").date()

today = date.today()

colS,colE = st.sidebar.columns(2)

with colS:
    selected_start_date = colS.date_input("Start date",
                                    date(2025, 3, 23),
                                    min_value = date(1949, 9, 7),
                                    max_value = today
                                    )

with colE:
    selected_end_date = colE.date_input("End date",
                                    date.today(),
                                    max_value=today,
                                    min_value= date(1949, 9, 7)
                                    )
if selected_end_date < selected_start_date:
    st.sidebar.write(
        "Invalid selection, showing current Wahlperiode!"
    )

wahl_start = date(2025, 3, 23)
final_start_date = wahl_start
final_end_date = today

# st.write(bundestag_periods.get(21))
# date_2 = bundestag_periods.get(21)[1]

for period in bundestag_periods:
    date_1 = string_to_date(s= (bundestag_periods.get(period)[0]))
    date_2 = string_to_date(s= (bundestag_periods.get(period)[1]))

    if date_1 <= selected_start_date <= date_2:
        if date_1 <= selected_end_date <= date_2:
            if selected_end_date >= selected_start_date:
                final_start_date = selected_start_date
                final_end_date = selected_end_date
        else:
            st.sidebar.write(
                "Invalid selection, current Wahlperiode showing :) "
            )

st.write(
    final_start_date, final_end_date
)

st.write("Comparing speeches from:", final_start_date, 'to', final_end_date)

# if 'final_start_date' not in st.session_state:
#     st.session_state.final_start_date = final_start_date

# if 'final_end_date' not in st.session_state:
#     st.session_state.final_end_date = final_end_date
st.session_state.final_start_date = final_start_date
st.session_state.final_end_date = final_end_date
