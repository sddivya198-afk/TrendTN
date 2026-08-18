import streamlit as st
from googleapiclient.discovery import build
import pandas as pd

st.set_page_config(page_title="TrendTN", layout="wide")

# 1. KEY AH SECRETS LA IRUNDHU EDUTHUKURADHU
YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]

# 2. YOUTUBE CONNECT PANNURADHU
@st.cache_resource
def get_youtube():
    return build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

youtube = get_youtube()

st.title("🔥 TrendTN - Tamil YouTube Trending")
st.write("Tamil Nadu la ipo trending aagura videos")

# 3. TRENDING VIDEOS EDUTHU KAATUDHU
@st.cache_data(ttl=600) # 10 nimishathukku oru thadava update aagum
def get_trending_tn():
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="IN", # India
        maxResults=20
    )
    response = request.execute()
    return response["items"]

try:
    videos = get_trending_tn()
    for video in videos:
        title = video["snippet"]["title"]
        channel = video["snippet"]["channelTitle"]
        views = int(video["statistics"]["viewCount"])
        thumbnail = video["snippet"]["thumbnails"]["medium"]["url"]
        video_id = video["id"]
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(thumbnail)
        with col2:
            st.subheader(title)
            st.write(f"**Channel:** {channel}")
            st.write(f"**Views:** {views:,}")
            st.markdown(f"[Watch Video](https://www.youtube.com/watch?v={video_id})")
        st.divider()

except Exception as e:
    st.error(f"Error: {e}")
