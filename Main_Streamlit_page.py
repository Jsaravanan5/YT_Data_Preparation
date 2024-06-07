import streamlit as st
import pandas as pd
from googleapiclient.discovery import build


def main():
    st.title(":red[YOUTUBE HARVESTING AND DATA WAREHOUSING]")
    st.write("YouTube Data Harvesting and Warehousing project - Provide you the youtube channel details,playlist details,video details and comment details")
    st.header(":movie_camera: Youtube Channel Collection")
    st.page_link("https://ytdatapreparation-cv68zz4dmo9reqjpa8beyw.streamlit.app/",icon='👉',label=':red-background[CLICK HERE FOR YOUTUBE CHANNEL COLLECTION]')
    
    st.header(":question:&:pencil: Queries & Result")
    st.write("***Analyze Based on the Given Question***")
    st.page_link("https://ytdatapreparation-n8dkghsqzccsyvr86zt3ee.streamlit.app/",icon='👉',label=':red-background[CLICK HERE FOR QUERY & RESULT]')
if __name__ == "__main__":
    main()
