import streamlit as st
import requests
import pandas as pd

from params import *

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

response = requests.get(f"{API_URL}/parameters").json()

################################### Main Page ##########################################
st.write(
    "<h1 style='text-align: center;'>Practice What You Preach</h1>",
    unsafe_allow_html=True
    )
st.space('large')
st.write(
    "Welcome to our website, where you can compare what politicians claim they are invested in, and how that matches their behaviour when they show up to the Bundestag.",
    unsafe_allow_html=True
    )
st.write(
    "Do the political parties really put their money where their mouth is?",
    unsafe_allow_html=True
    )
st.space('medium')
st.write(
    "Select a political topic from the navigation bar on the left to compare how each major party checks out.",
    unsafe_allow_html=True
    )
st.write(
    "If no dates are chosen, the current Wahlperiode dates will be used. Below is a list of the Wahlperioden and their respective dates.",
    unsafe_allow_html=True
    )

################################### Wahlperiode Chart ##########################################
bundestag_periods = response['bundestag_wahlperiode']
wahlperioden = (pd.DataFrame(bundestag_periods,
                            index=["Start Date","End Date"]
                            )).T

st.table(wahlperioden)
