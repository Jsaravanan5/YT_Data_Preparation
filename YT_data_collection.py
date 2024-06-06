import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import mysql.connector
import streamlit as st
#pip install/upgrade google-api-python-client
import googleapiclient.discovery


def get_youtube_api_client():
  api_key= 'AIzaSyDjcDOnrVqFSzMJUqNk53owwiZZr6zsxQQ'
  api_service_name = "youtube"
  api_version = "v3"
  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
  return youtube

youtube = get_youtube_api_client()


channel_id=input("Enter channel_id:")
#Function to get channel_info:
#def channels_info(channel_id):
request = youtube.channels().list(part="snippet,contentDetails,statistics,status",id=channel_id)
response1 = request.execute()

for channel_details in (response1['items']):
 channel_id=channel_details['id']
 Channel_Name=channel_details['snippet']['title']
 #Channel_type=channel_details['snippet']['type']
 Channel_views=channel_details['statistics']['viewCount']
 Channel_description=channel_details['snippet']['description']
 Overall_Playlist_ID=channel_details['contentDetails']['relatedPlaylists']['uploads']


#Pandas Dataframe

Channel_info_df=pd.DataFrame({'Channel_Id':[channel_id],'Channel_Name':[Channel_Name],'Channel_views':[Channel_views],'Channel_description':[Channel_description],'Overall_Playlist_ID':[Overall_Playlist_ID]})

print(Channel_info_df)


#Playlist ID :Table
request2= youtube.playlists().list(
        channelId="UC3LD42rjj-Owtxsa6PwGU5Q",part="snippet,contentDetails,status",maxResults=50)
response2=request2.execute()
response2

Playlist_Id_Title=[]
Playlist_Id=[]
Channel_Id=[]

for Playlist_Details in (response2['items']):
 Playlist_id_title=Playlist_Details['snippet']['title']
 Playlist_id=Playlist_Details['id']
 Playlist_Id.append(Playlist_id)
 Playlist_Id_Title.append(Playlist_id_title)
 channel_id=Playlist_Details['snippet']['channelId']
 Channel_Id.append(channel_id)


data={
    'Channel_Id':Channel_Id,
    'Playlist_id':Playlist_Id,
    'Playlist_id_title':Playlist_Id_Title

   }

df=pd.DataFrame(data)
print(df)