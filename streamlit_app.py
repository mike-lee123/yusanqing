"""雨傘情 動態曲譜（伴奏版）— a single-page Streamlit app that plays the sing-along video."""
from pathlib import Path

import streamlit as st

HERE = Path(__file__).parent
VIDEO = HERE / "media" / "yusanqing_accompaniment.mp4"
SCORE = HERE / "media" / "yusanqing_score.png"

st.set_page_config(page_title="雨傘情 動態曲譜", page_icon="☂️", layout="centered")


@st.cache_data
def load_bytes(path: Path) -> bytes:
    # read once per server process instead of on every rerun / every visitor
    return path.read_bytes()


st.title("☂️ 雨傘情　動態曲譜")
st.caption("黃中原 詞曲 · 黃乙玲 演唱 · 1=♭D　3/4　Waltz　｜　伴奏版")

st.video(load_bytes(VIDEO), format="video/mp4")

st.markdown(
    "跟著畫面唱：正在唱的音會亮起來，唱過的音符和歌詞會由左到右變成橘色。"
    "下方預告的是接下來要唱的那一行，遇到反覆或 D.S. 時會直接顯示要跳去的地方。"
)

with st.expander("📄 完整簡譜"):
    st.image(load_bytes(SCORE), width="stretch")

col1, col2 = st.columns(2)
col1.download_button("⬇️ 下載影片（MP4）", load_bytes(VIDEO),
                     file_name="雨傘情_動態曲譜_伴奏.mp4", mime="video/mp4", width="stretch")
col2.download_button("⬇️ 下載簡譜（PNG）", load_bytes(SCORE),
                     file_name="雨傘情_數位簡譜.png", mime="image/png", width="stretch")
