import streamlit as st
from backend import FoundationModel, XConnector, BskyConnector, FoundationModel
from frontend import model_prompt_tab, multiple_posts_tab, single_post_tab


# Define session state variables


# Prepare frontend
with st.sidebar():
    st.session_state.social_media = st.selectbox(
        label = "Select social media",
        options = ["Bsky","X"]
    )

tab1, tab2, tab3 = st.tabs()

with tab1:
    single_post_tab()

with tab2:
    multiple_posts_tab()

with tab3:
    model_prompt_tab()


# Define flow
def main():
    frontend()
    backend()

if __name__ == 'main':
    main()