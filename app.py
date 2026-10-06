import streamlit as st

st.set_page_config(page_title="防災士クイズ", page_icon="🚨", layout="centered")

# 章別カラー
CHAPTER_COLORS = {
    "地震・津波": "#1E88E5",
    "気象災害": "#00ACC1",
    "土砂災害": "#8D6E63",
    "火災・風水害": "#E53935",
    "避難行動": "#FB8C00",
    "避難所運営": "#43A047",
    "応急手当": "#D81B60",
    "地区防災計画": "#5E35B1",
    "BCP": "#3949AB",
    "最新災害": "#00897B",
    "弱点克服": "#546E7A",
}

# スマホ向けCSS
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        padding: 14px;
        font-size: 1.1rem;
        border-radius: 10px;
    }
    .stRadio>div {
        font-size: 1.0rem;
    }
</style>
""", unsafe_allow_html=True)


def init_state():
    if "total_questions" not in st.session_state:
        st.session_state.total_questions = {}
    if "total_correct" not in st.session_state:
        st.session_state.total_correct = {}
    if "wrong_all" not in st.session_state:
        st.session_state.wrong_all = []


def run_quiz(quiz, chapter_name):
    init_state()

    if chapter_name not in st.session_state.total_questions:
        st.session_state.total_questions[chapter_name] = 0
        st.session_state.total_correct[chapter_name] = 0

    correct_count = 0

    for i, q in enumerate(quiz, start=1):
        st.markdown(f"### Q{i}. {q['question']}")
        choice = st.radio("選択肢", q["options"], key=f"{chapter_name}_{i}")

        if st.button(f"この問題の答えを見る", key=f"btn_{chapter_name}_{i}"):
            if choice == q["answer"]:
                st.success("正解！")
                correct_count += 1
            else:
                st.error(f"不正解… 正解は「{q['answer']}」です。")
                st.session_state.wrong_all.append(q)

            st.info(q["explanation"])

        st.markdown("---")

    # 集計更新
    st.session_state.total_questions[chapter_name] += len(quiz)
    st.session_state.total_correct[chapter_name] += correct_count

    st.markdown("## この章の結果")
    st.write(f"出題数：{len(quiz)}問")
    st.write(f"正解数：{correct_count}問")
    rate = int(correct_count / len(quiz) * 100)
    st.write(f"正答率：{rate}%")
    st.progress(rate / 100)


# メインページ（任意）
def main():
    st.title("防災士クイズアプリ")
    st.write("左のメニューから章を選んでください。")


if __name__ == "__main__":
    main()
