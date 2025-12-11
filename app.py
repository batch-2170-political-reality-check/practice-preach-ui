from datetime import date, datetime
import streamlit as st
import requests

from params import API_URL

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

url = f"{API_URL}/parameters"

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

#################################### Topic Navigation #########################

# FIXME So… we went for a st.navigation and don't want drop-downs. But
# st.navigation takes pages which don't take any query-params... I tried to use
# https://docs.streamlit.io/develop/api-reference/widgets/st.page_link, but
# that didn't fit into a navigation...
pages = [
        st.Page("Home.py", title="Home"),
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

pg = st.navigation(pages)
pg.run()

################################### Sidebar Dates ##########################
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

if final_end_date >= date(2025, 12, 11):
    final_end_date = date(2025,12,10)

st.write("Comparing speeches from:", final_start_date, 'to', final_end_date)

st.session_state.final_start_date = final_start_date
st.session_state.final_end_date = final_end_date
