import streamlit as st
import pandas as pd
#from googleapiclient.discovery import build

def main():
    st.title(":red[YOUTUBE HARVESTING AND DATA WAREHOUSING]")
    st.write("The YouTube Data Harvesting and Warehousing project aims to empower users by allowing them to access and analyze data from various YouTube channels. The project utilizes SQL and Streamlit to develop a user-friendly application that enables users to retrieve, save, and query YouTube channel and video data")

    st.header(":movie_camera: Youtube Channel Collection")
    st.write(".")
    st.header(":question:&:pencil: Queries & Result")
    st.write("channel details,playlist details,comment details and video details")
    st.page_link("https://ytdatapreparation-3wcalt7bzmbzuiegak5zs4.streamlit.app/",icon='👉',label=':red-background[CLICK HERE]')
if __name__ == "__main__":
    main()
