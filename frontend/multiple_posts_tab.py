import streamlit as st
from datetime import datetime, timedelta, date


def multiple_posts_tab():
    
    st.session_state.date_range_multiple_posts = st.date_input(
        label = 'Date range for posts to be fetched',
        value = (
                (date.today() - timedelta(days=7)).strftime("%Y-%m-%d"), 
                date.today().strftime("%Y-%m-%d")
            )
    )

    st.session_state.fetch_list_of_posts = st.button(
        label = "Fetch list of posts from Telegram"
    )

    st.session_state.prepare_list_of_posts = st.button(
        label = "Prepare captions for posts"
    )

    st.session_state.download_list_of_posts = st.button(
        label = "Download list of posts"
    )