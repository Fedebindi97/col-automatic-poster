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

    prepare_list_of_posts = st.button(
        label = "Fetch and prepare list of posts"
    )

    download_list_of_posts = st.button(
        label = "Download list of posts"
    )