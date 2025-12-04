import streamlit as st
from datetime import datetime, date
import requests
# import bundestag_periods

#################################### Page Configs   #########################################
st.set_page_config(
    page_title="Practice What You Preach",
    page_icon=":material/edit:",
    layout='wide'
    )

topics = ["Climate","Digital","MettIgel"]

# pg = st.navigation(topics)
# pg.run()

# pages = {
#     "Bob": [
#         st.Page("page_1.py", title="Create your account")
#     ],
#     "Carl": [
#         st.Page("page_2.py", title="Learn about us")
#     ],
# }

# pg = st.navigation(pages)
# # pg.run()


################################### Main Page ##########################################
st.markdown("<h1 style='text-align: center;'>Practice What You Preach</h1>", unsafe_allow_html=True)

def function_for_tile_1():
    st.session_state.current_view = "view_1"

def function_for_tile_2():
    st.session_state.current_view = "view_2"

# Initialize session state for managing views if not already set
if 'current_view' not in st.session_state:
    st.session_state.current_view = "menu"

st.header("Select an Option")

col1, col2 = st.columns(2)



with col1:
    # Use a container or simply place a button to act as a "tile"
    container_1 = st.container(border=True)
    container_1.markdown(
        "The party's platform emphasizes **urgent action on climate change**, recognizing it as a **significant threat to global security and economic stability**. They advocate for a **transition to renewable energy sources** and **investment in green technologies**. The party also supports **international cooperation** to address the climate crisis and calls for **stricter environmental regulations** to reduce greenhouse gas emissions. Furthermore, they propose **carbon pricing mechanisms** and **incentives for sustainable practices** across industries."
        )

    # if st.button("Tile 1: Go to View 1", use_container_width=True):
    #     function_for_tile_1()

with col2:
    st.write(
        "The party's platform emphasizes **urgent action on climate change**, recognizing it as a **significant threat to global security and economic stability**. They advocate for a **transition to renewable energy sources** and **investment in green technologies**. The party also supports **international cooperation** to address the climate crisis and calls for **stricter environmental regulations** to reduce greenhouse gas emissions. Furthermore, they propose **carbon pricing mechanisms** and **incentives for sustainable practices** across industries."
        )


################################### Sidebar ##########################################
st.divider()

st.sidebar.write("Choose a time period within Wahlperiode dates.")
st.sidebar.write("Default time period is 1 Wahlperiode")

bundestag_periods = {
    1:  (date(1949, 9, 7),  date(1953, 10, 6)),
    2:  (date(1953, 10, 6), date(1957, 10, 15)),
    3:  (date(1957, 10, 15), date(1961, 10, 17)),
    4:  (date(1961, 10, 17), date(1965, 10, 19)),
    5:  (date(1965, 10, 19), date(1969, 10, 20)),
    6:  (date(1969, 10, 20), date(1972, 12, 13)),
    7:  (date(1972, 12, 13), date(1976, 12, 13)),
    8:  (date(1976, 12, 13), date(1980, 11, 4)),
    9:  (date(1980, 11, 4), date(1983, 3, 29)),
    10: (date(1983, 3, 29), date(1987, 2, 18)),
    11: (date(1987, 2, 18), date(1990, 12, 20)),
    12: (date(1990, 12, 20), date(1994, 11, 10)),
    13: (date(1994, 11, 10), date(1998, 10, 26)),
    14: (date(1998, 10, 26), date(2002, 10, 17)),
    15: (date(2002, 10, 17), date(2005, 10, 18)),
    16: (date(2005, 10, 18), date(2009, 10, 27)),
    17: (date(2009, 10, 27), date(2013, 10, 22)),
    18: (date(2013, 10, 22), date(2017, 10, 24)),
    19: (date(2017, 10, 24), date(2021, 10, 26)),
    20: (date(2021, 10, 26), date(2025, 3, 22)),
    21: (date(2025, 3, 23), date.today())  # still ongoing
}

today = date.today()

selected_start_date = st.sidebar.date_input("Start date",
                                   date(2025, 2, 1),
                                   min_value = date(1949, 9, 7),
                                   max_value = today
                                   )

selected_end_date = st.sidebar.date_input("End date",
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
    date_1 = bundestag_periods.get(period)[0]
    date_2 = bundestag_periods.get(period)[1]
    if date_1 <= selected_start_date <= date_2:
        if date_1 <= selected_end_date <= date_2:
            if selected_end_date > selected_start_date:
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
