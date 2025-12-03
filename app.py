import streamlit as st
from src.ui.dashboard import render_dashboard

st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide"
)

render_dashboard()