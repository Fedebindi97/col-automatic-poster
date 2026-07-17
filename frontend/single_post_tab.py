import streamlit as st


def single_post_tab(social_network):
    
    col1, col2 = st.columns(2)

    with col1:
        st.session_state.post_raw_text = st.text_area(
            label = "Text to be rewritten"
        )

    with col2:
        st.session_state.image_files = st.file_uploader(
            label = "Image(s)",
            accept_multiple_files = True
        )

    create_single_post = st.button(
        label = "Rewrite text",
        disabled = st.session_state.post_raw_text == ''
    )

    with st.container(height = 350):
        pass
        #st.write(st.session_state.post_rewritten_text)

    post_to_social_network = st.button(
        label = "Post to " + social_network,
        disabled = True#st.session_state.post_rewritten_text == ''
    )

    