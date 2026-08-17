import streamlit as st
from youtubesearchpython import VideosSearch
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="TrendTN", page_icon="🔥")
st.title("🔥 TrendTN")
st.write("Warning illaama clear ah Tamil Nadu trending paaru")

st.header("Today's TN Trends - " + datetime.now().strftime("%d %b %Y"))

# YouTube Trending
st.subheader("YouTube TN Trending")
try:
    videosSearch = VideosSearch("Tamil Nadu trending", limit=5)
    result = videosSearch.result()
    for i, video in enumerate(result['result'], 1):
        st.write(f"{i}. {video['title']} - {video['channel']['name']}")
except:
    st.write("YouTube data loading...")

st.success("App is running!")
