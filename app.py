import streamlit as st
from backend import FoundationModel, XConnector, BskyConnector, FoundationModel, SYSTEM_INSTRUCTIONS
from frontend import model_prompt_tab, multiple_posts_tab, single_post_tab
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


# Define session state variables


# Prepare frontend
st.set_page_config(
    page_title = 'CoL - AI social media assistant',
    page_icon = ':fish:'
)

st.title(
    'Coast of Life - AI social media assistant'
)

with st.sidebar:
    st.session_state.social_network = st.selectbox(
        label = "Select social network",
        options = ["Bluesky","X"]
    )

tab1, tab2, tab3 = st.tabs(["Convert a single post", "Convert list of posts from the Telegram channel", "Update LLM prompt"])

with tab1:
    single_post_tab(st.session_state.social_network)

with tab2:
    multiple_posts_tab()

with tab3:
    model_prompt_tab(baseline_prompt=SYSTEM_INSTRUCTIONS.format(social_network=st.session_state.social_network))