import streamlit as st
import pandas as pd
from datetime import datetime
from yt_dlp import YoutubeDL

st.set_page_config(page_title="TrendTN", layout="centered")

st.title("🔥 TrendTN")
st.caption("Warning illaama clear ah Tamil Nadu trending paaru")
st.header(f"Today's TN Trends - {datetime.now().strftime('%d %b %Y')}")
st.subheader("YouTube TN Trending")

@st.cache_data(ttl=3600)
def get_trending():
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'skip_download': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        # India Trending page ah direct ah edukum
        results = ydl.extract_info("https://www.youtube.com/feed/trending", download=False)
        videos = []
        if results and 'entries' in results:
            for item in results['entries'][:15]: # first 15 videos
                if item:
                    videos.append({
                        "Title": item.get('title', 'No Title'),
                        "Channel": item.get('uploader', 'N/A'),
                        "Link": f"https://youtube.com/watch?v={item['id']}"
                    })
    return pd.DataFrame(videos)

try:
    df = get
