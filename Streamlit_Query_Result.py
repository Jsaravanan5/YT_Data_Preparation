import pandas as pd
import googleapiclient.discovery
import streamlit as st
import datetime
import matplotlib.pyplot as plt
import mysql.connector


# MySQL connection configuration
mysql_host = "localhost"
mysql_user = "sqluser"
mysql_password = "password"
mysql_database = "youtubedatabase"
mysql_port = "3306"

# Function to connect to MySQL database
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database,
            port=mysql_port
        )
        print("Connected to youtubedatabase successfully")
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to youtubedatabase :", e)
        return None


def execute_query(query):
    mydb = mysql.connector.connect(
        host="localhost",
        user="sqluser",
        password="password",
        database="youtubedatabase",
        port="3306"
    )
    cursor = mydb.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    mydb.close()
    return data


st.image("https://upload.wikimedia.org/wikipedia/commons/9/90/Logo_of_YouTube_%282013-2015%29.svg", caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
st.title(":red[Youtube_Channel_Analysis]")
st.text("WELCOME EVERYONE")

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

if Question == "1.What are the names of all the videos and their corresponding channels?":
     query = """
        SELECT c.Channel_Name, v.Title 
        FROM channel_data AS c 
        JOIN video_data AS v 
        ON c.Channel_Id = v.Channel_Id;
    """
     result = execute_query(query)
     df = pd.DataFrame(result, columns=["Channel_Name","Title"])
     st.dataframe(df,hide_index=True)

elif Question == "Which channels have the most number of videos, and how many videos do they have?":
        query = """
            SELECT Channel_Name, Total_videos 
            FROM channel_data
            ORDER BY Total_videos DESC;
        """
        result = execute_query(query)
        df1 = pd.DataFrame(result, columns=["Channel_Name", "Total_videos"])
        st.dataframe(df1,hide_index=True)
        # st.write(df1)




elif Question == "What are the top 10 most viewed videos and their respective channels?":
        query = """
                select Channel_Name,Title,Views from video_data
                order by Views desc limit 10;
                """
        result = execute_query(query)
        df2 = pd.DataFrame(result, columns=["Channel_Name", "Title","Views"])
        st.dataframe(df2,hide_index=True)
        # st.write(df2)



elif Question == "How many comments were made on each video, and what are their corresponding video names?" :
        query = """
                Select c.Channel_Name, v.comments,v.Title from channel_data as c join video_data as v on c.Channel_ID=v.Channel_ID;
                """
        result = execute_query(query)
        df3 = pd.DataFrame(result, columns=["Channel_Name", "Comments","Title"])
        # st.write(df3)
        st.dataframe(df3,hide_index=True)



elif Question == "Which videos have the highest number of likes, and what are their corresponding channel names?" :
        query = """
                select c.Channel_Name,v.Title,v.Likes from channel_data as c join video_data as v on c.Channel_ID=v.Channel_ID
                order by v.Likes desc;
                """
        result = execute_query(query)
        df4 = pd.DataFrame(result, columns=["Channel_Name", "Title","Likes"])
        # st.write(df4)
        st.dataframe(df4,hide_index=True)


elif Question == "What is the total number of likes for each video, and what are their corresponding video names?" :
        query = """
                SELECT Title, SUM(Likes) AS Total_Likes
                FROM video_data
                GROUP BY Title
                ORDER BY Total_Likes DESC;
                """
        result = execute_query(query)
        df5 = pd.DataFrame(result, columns=[ "Title","Likes"])
        # st.write(df5)
        st.dataframe(df5,hide_index=True)




elif Question == "What is the total number of views for each channel, and what are their corresponding channel names?" :
        query = """
                select Channel_Name,views from channel_data order by views desc;
                """
        result = execute_query(query)
        df6 = pd.DataFrame(result, columns=[ "Channel_Name","views"])
        # st.write(df6)
        st.dataframe(df6,hide_index=True)



elif Question == "What are the names of all the channels that have published videos in the year 2022?" :
        query = """
                select Channel_Name from video_data
                where EXTRACT(YEAR FROM Publishdate) = 2022;
                """
        result = execute_query(query)
        df7 = pd.DataFrame(result, columns=[ "Channel_Name"])
        # st.write(df7)
        st.dataframe(df7,hide_index=True)





elif Question == "What is the average duration of all videos in each channel, and what are their corresponding channel names?" :
        query = """
                SELECT c.Channel_Name, AVG(v.Duration) AS Avg_Duration
                FROM channel_data c
                JOIN video_data v ON c.Channel_Id = v.Channel_Id
                GROUP BY c.Channel_Name;
                """
        result = execute_query(query)
        df8 = pd.DataFrame(result, columns=[ "Channel_Name","Avg_Duration"])
        # st.write(df8)
        st.dataframe(df8,hide_index=True)




elif Question == "Which videos have the highest number of comments, and what are their corresponding channel names?" :
        query = """
                SELECT c.Channel_Name, v.Title, COUNT(co.Comment_Id) AS Num_Comments
                FROM channel_data c
                JOIN video_data v ON c.Channel_Id = v.Channel_Id
                LEFT JOIN comment_data co ON v.Video_Id = co.Video_Id
                GROUP BY c.Channel_Name, v.Title
                ORDER BY Num_Comments DESC
                LIMIT 10;
                """
        result = execute_query(query)
        df9 = pd.DataFrame(result, columns=[ "Channel_Name","Title","Num_Comments"])
        # st.write(df9)
        st.dataframe(df9,hide_index=True)








