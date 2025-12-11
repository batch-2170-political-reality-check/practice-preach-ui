from datetime import date
import streamlit as st
import requests
# from PIL import Image

from params import *

# ################################# Topic API Call ##########################################
response = requests.get(f"{API_URL}/parameters").json()

topic_list = list(response['political_topics'].keys())
for i in range(len(topic_list)):
    topic_list[i] = topic_list[i].replace('_',' ')
    if ' ' in topic_list[i]:
        g = topic_list[i].split(' ')
        for h in range(len(g)):
            g[h] = g[h].capitalize()
        topic_list[i] = ' '.join(g)
    else:
        topic_list[i] = topic_list[i].capitalize()


topics = sorted(topic_list)
topic = topics[6]
topic_q = topic.lower()
#################################### Page Configs   #########################################
st.set_page_config(
    page_title=topic,
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

# ################################# Date Selection Grab ##########################################

if 'final_start_date' in st.session_state:
    final_start_date = st.session_state.final_start_date
else:
    final_start_date = date(2025,3,23)

if 'final_end_date' in st.session_state:
    final_end_date = st.session_state.final_end_date
else:
    final_end_date = date(2025,3,23)

# ################################# Speech API Call ##########################################

with st.spinner("Hold your :horse: :horse: :horse:...", show_time=True):
    params = {
        'start_date': date2str(final_start_date),
        'end_date': date2str(final_end_date),
        'topic': topic_q,
    }

    response2 = requests.get(f"{API_URL}/summaries",params=params).json()

################################### Main Page ##########################################
st.markdown(f"""<h1 style='text-align: center;'> {topic} </h1>""", unsafe_allow_html=True)
st.space("small")

col1, col2 = st.columns(2, gap='medium')
st.space("small")
col3, col4 = st.columns(2, gap='medium')
st.space("small")
col5, col6 = st.columns(2, gap='medium')

height = 300
st.write(
    final_start_date,
    final_end_date
)
with col1:
    st.write("AfD - Alternative for Deutschland")

    container_1 = st.container(
        border=True,
        horizontal_alignment='distribute',
        vertical_alignment='distribute',
        height = height

        )

    container_1.markdown(
        response2['AfD']['summary'],
        unsafe_allow_html=True
        )
    # col1a = st.columns(1)

    # with col1a:
    container_1a = st.container(
        border=True,
        horizontal=True,
        # horizontal_alignment='distribute',
        # vertical_alignment='distribute',
        height = 50,
        width= 1000

    )

    container_1a.write(
        response2['AfD']['label']
    )

    # with col1b:
        # container_1b = st.container(
        #     border=True,
        #     horizontal_alignment='distribute',
        #     vertical_alignment='distribute',
        #     height = 30,
        #     width= 100
        # )
        # col1b.image(img_g)

with col2:
    st.write("B90 - Die Grünen")

    container_2 = st.container(
        border=True,
        horizontal_alignment='distribute',
        vertical_alignment='distribute',
        height = height
        )
    container_2.write(
        response2['BÜNDNIS 90/DIE GRÜNEN']['summary'],
        unsafe_allow_html=True
        )

    container_2a = st.container(
        border=True,
        horizontal=True,
        # horizontal_alignment='distribute',
        # vertical_alignment='distribute',
        height = 50,
        width= 1000

    )

    container_2a.write(
        response2['BÜNDNIS 90/DIE GRÜNEN']['label']
    )

st.space("medium")

with col3:
    st.write("CDU - Christian Democratic Union")

    container_3 = st.container(
        border=True,
        horizontal_alignment='distribute',
        vertical_alignment='distribute',
        height = height
        )
    container_3.write(
        response2['CDU/CSU']['summary'],
        unsafe_allow_html=True
        )

    container_3a = st.container(
        border=True,
        horizontal=True,
        # horizontal_alignment='distribute',
        # vertical_alignment='distribute',
        height = 50,
        width= 1000

    )

    container_3a.write(
        response2['CDU/CSU']['label']
    )


with col4:
    st.write("Die Linke")

    container_4 = st.container(
        border=True,
        horizontal_alignment='distribute',
        vertical_alignment='distribute',
        height = height
        )
    container_4.write(
        response2['Die Linke']['summary'],
        unsafe_allow_html=True
        )

    container_4a = st.container(
        border=True,
        horizontal=True,
        # horizontal_alignment='distribute',
        # vertical_alignment='distribute',
        height = 50,
        width= 1000

    )

    container_4a.write(
        response2['Die Linke']['label']
    )

with col5:
    st.write("SPD - Social Democratic Party")


    container_5 = st.container(
        border=True,
        horizontal_alignment='distribute',
        vertical_alignment='distribute',
        height = height
        )
    container_5.write(
        response2['SPD']['summary'],
        unsafe_allow_html=True
        )

    container_5a = st.container(
        border=True,
        horizontal=True,
        # horizontal_alignment='distribute',
        # vertical_alignment='distribute',
        height = 50,
        width= 1000

    )

    container_5a.write(
        response2['SPD']['label']
    )
