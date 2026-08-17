import streamlit as st
from youtube_search import VideosSearch
import pandas as pd
from datetime import datetime

@st.cache_data(ttl=1800)  # 30 min ku oru thadava dhan YouTube ah ketkum
def get_trending():
    videosSearch = VideosSearch("", region="IN", lang="ta", limit=10)
    return videosSearch.result()['result']

st.set_page_config(page_title="TrendTN", page_icon="🔥")
st.title("🔥 TrendTN")
st.write("Warning illaama clear ah Tamil Nadu trending paaru")

st.header("Today's TN Trends - " + datetime.now().strftime("%d %b %Y"))

st.subheader("YouTube TN Trending")
try:
    result = get_trending()
    for i, video in enumerate(result, 1):
        st.write(f"{i}. {video['title']} - {video['channel']['name']}")
except:
    st.write("YouTube data loading...")

st.success("App is running!")
