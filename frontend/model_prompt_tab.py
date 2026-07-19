import streamlit as st

def model_prompt_tab(baseline_prompt):
    st.session_state.llm_system_instructions = st.text_area(
            label = "LLM prompt",
            value = baseline_prompt,
            height = 400
        )
