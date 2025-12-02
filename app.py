# def main():
#     print("Hello from practce-preach-ui!")


# if __name__ == "__main__":
#     main()

import streamlit as st

st.set_page_config(page_title="Practice What You Preach", page_icon=":material/edit:")

'''
# Practice What You Preach
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
