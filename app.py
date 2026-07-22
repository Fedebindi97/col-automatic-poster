import streamlit as st
from backend import SocialMediaPost, SocialMediaPostCollection, TelegramConnector, XConnector, BskyConnector, APIModel, LocalModel, SYSTEM_INSTRUCTIONS
from frontend import model_prompt_tab, multiple_posts_tab, single_post_tab
import configparser

from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LOCAL = True
config = configparser.ConfigParser()
config.read('config.ini')
LOCAL = config.getboolean('DEFAULT', 'local', fallback=LOCAL)

# Initialize session state variables, if needed
if 'post_rewritten_text' not in st.session_state:
    st.session_state.post_rewritten_text = ''

# Define useful objects
if LOCAL:
    st.session_state.foundation_model = LocalModel()
else:
    st.session_state.foundation_model = APIModel(
        gemini_api_key = GEMINI_API_KEY, 
        system_instructions = st.session_state.llm_system_instructions
    )
st.session_state.telegram_connector = TelegramConnector()

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

if st.session_state.social_network == 'Bluesky':
    st.session_state.social_network_connector = BskyConnector()
else:
    st.session_state.social_network_connector = XConnector()

tab1, tab2, tab3 = st.tabs(["Convert a single post", "Convert list of posts from the Telegram channel", "Update LLM prompt"])

with tab1:
    single_post_tab(st.session_state.social_network)
    if st.session_state.create_single_post:
        st.session_state.post_rewritten_text = st.session_state.foundation_model.generate_text(
            st.session_state.post_raw_text,
            st.session_state.image_files
        )
        st.session_state.post_to_share = SocialMediaPost(
            text = st.session_state.post_rewritten_text,
            images = st.session_state.image_files
        )
        st.rerun()
    if st.session_state.post_to_social_network:
        st.session_state.social_network_connector.post(
            st.session_state.post_to_share
        )
        st.success('Post shared on' + st.session_state.social_network + '!')

with tab2:
    multiple_posts_tab()
    if st.session_state.fetch_list_of_posts:
        raw_lists_texts_images = st.session_state.telegram_connector.fetch_posts_from_telegram_channel(
            date_start = st.session_state.date_range_multiple_posts[0],
            date_end = st.session_state.date_range_multiple_posts[1]
        )
        st.session_state.posts_collection = SocialMediaPostCollection(
            raw_texts_images = raw_lists_texts_images
        )
    if st.session_state.prepare_list_of_posts:
        st.session_state.posts_collection.prepare_posts(st.session_state.foundation_model)
    if st.session_state.download_list_of_posts:
        st.session_state.posts_collection.download_posts()

with tab3:
    model_prompt_tab(
        baseline_prompt=SYSTEM_INSTRUCTIONS.format(social_network=st.session_state.social_network)
    )