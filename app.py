import streamlit as st
from backend import TelegramConnector, FoundationModel, XConnector, BskyConnector, APIModel, LocalModel, SYSTEM_INSTRUCTIONS
from frontend import model_prompt_tab, multiple_posts_tab, single_post_tab
import configparser

from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

config = configparser.ConfigParser()
config.read('config.ini')
LOCAL = config['DEFAULT']['local']


# Define useful objects
if LOCAL:
    st.session_state.foundation_model = LocalModel()
else:
    st.session_state.foundation_model = APIModel(
        gemini_api_key = GEMINI_API_KEY, 
        system_instructions = st.session_state.llm_system_instructions
    )
st.session_state.telegram_connector = TelegramConnector()
if st.session_state.social_network == 'Bluesky':
    social_network_connector = BskyConnector()
else:
    social_network_connector = XConnector()

# App flow
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
    #convert post, post post

with tab2:
    multiple_posts_tab()
    # get posts

with tab3:
    model_prompt_tab(baseline_prompt=SYSTEM_INSTRUCTIONS.format(social_network=st.session_state.social_network))