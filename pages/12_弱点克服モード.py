import streamlit as st
from app import run_quiz, CHAPTER_COLORS, init_state

chapter_name = "弱点克服"
color = CHAPTER_COLORS[chapter_name]

st.markdown(f"<h1 style='color:{color}'>🔁 弱点克服モード</h1>", unsafe_allow_html=True)

init_state()

if len(st.session_state.wrong_all) == 0:
    st.info("まだ間違えた問題がありません。各章のクイズを先に解いてください。")
else:
    st.write(f"間違えた問題数：{len(st.session_state.wrong_all)}問")
    run_quiz(st.session_state.wrong_all, chapter_name)
