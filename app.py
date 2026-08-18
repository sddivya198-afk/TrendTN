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
        'noplaylist': True,
        'skip_download': True
    }
    with Youtube
