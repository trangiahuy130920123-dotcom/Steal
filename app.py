"""Steal An Egg 3D - chi embed game HTML
streamlit run app.py
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Steal An Egg 3D", page_icon="🥚", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{background:#0b1220}
.block-container{padding:0.15rem!important;max-width:100%!important}
#MainMenu,footer,header{visibility:hidden}
</style>
""", unsafe_allow_html=True)

game = Path(__file__).resolve().parent / "steal_an_egg.html"
if not game.exists():
    st.error("Thieu steal_an_egg.html")
    st.stop()

components.html(game.read_text(encoding="utf-8"), height=860, scrolling=False)
