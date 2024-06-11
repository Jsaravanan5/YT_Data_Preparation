import streamlit as st
import pandas as pd


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "Age": [10,20,30]
 } 

df=pd.DataFrame(data)
#print(df)

Question = st.selectbox(
    " Please select a question:",
    ("1.What are the names of all the videos and their corresponding channels?",
     "2.Which channels have the most number of videos, and how many videos do they have?",
     "3.What are the top 10 most viewed videos and their respective channels?",
     "4.How many comments were made on each video, and what are their corresponding video names",
     "5.Which videos have the highest number of likes, and what are their corresponding channel names?",
     "6.What is the total number of likes and dislikes for each video, and what are their corresponding video names?",
     "7.What is the total number of views for each channel, and what are their corresponding channel names?",
     "8.What are the names of all the channels that have published videos in the year 2022?",
     "9.What is the average duration of all videos in each channel, and what are their corresponding channel names?",
     "10.Which videos have the highest number of comments, and what are their corresponding channel names?"),
    )

if Question == "2.Which channels have the most number of videos, and how many videos do they have?":
    st.dataframe(df,hide_index=True)

