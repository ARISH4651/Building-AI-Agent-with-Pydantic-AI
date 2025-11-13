import streamlit as st
from agent_utils import get_search_results

st.set_page_config(page_title="🔍 GenAi Search Agent", page_icon="🤖")

st.title("🔍 GenAi Search Agent")

query = st.text-input("Enter your search query here...!")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching..."):
            response -get_search_results(query)
        st.success("✅ Here are the search results for you...")
        st.wrote(response)
    else:
        st.warning("⚠️Please enter a valid search query.")
