import streamlit as st
from app import CHAPTER_COLORS, init_state

st.markdown("<h1>📊 総合成績（全章の正答率）</h1>", unsafe_allow_html=True)

init_state()

if len(st.session_state.total_questions) == 0:
    st.info("まだクイズが実施されていません。左の章からクイズを始めてください。")
else:
    for chapter, total in st.session_state.total_questions.items():
        correct = st.session_state.total_correct.get(chapter, 0)
        rate = int(correct / total * 100) if total > 0 else 0
        color = CHAPTER_COLORS.get(chapter, "#000000")

        st.markdown(f"### <span style='color:{color}'>{chapter}</span>", unsafe_allow_html=True)
        st.write(f"- 出題数：{total}問")
        st.write(f"- 正解数：{correct}問")
        st.write(f"- 正答率：{rate}%")
        st.progress(rate / 100)
        st.markdown("---")
