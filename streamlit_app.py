"""雨傘情 動態曲譜（伴奏版）— a single-page Streamlit app that plays the sing-along video."""
from pathlib import Path

import streamlit as st

HERE = Path(__file__).parent

st.set_page_config(page_title="雨傘情 動態曲譜", page_icon="☂️", layout="centered")


def find(name: str):
    """GitHub's browser upload sometimes drops the media/ folder, so look anywhere in the repo."""
    hits = sorted(HERE.rglob(name))
    return hits[0] if hits else None


@st.cache_data
def load_bytes(path: str) -> bytes:
    # read once per server process instead of on every rerun / every visitor
    return Path(path).read_bytes()


VIDEO = find("yusanqing_accompaniment.mp4")
SCORE = find("yusanqing_score.png")

st.title("☂️ 雨傘情　動態曲譜")
st.caption("黃中原 詞曲 · 黃乙玲 演唱 · 1=♭D　3/4　Waltz　｜　伴奏版")

if VIDEO is None:
    files = sorted(str(p.relative_to(HERE)) for p in HERE.rglob("*") if p.is_file() and ".git" not in p.parts)
    st.error("找不到影片檔 **yusanqing_accompaniment.mp4**。請到 GitHub 把它上傳到這個 repository"
             "（放在最外層或 media 資料夾都可以），上傳後重新整理這個網頁。")
    st.write("目前 repository 裡的檔案：")
    st.code("\n".join(files) or "（沒有檔案）")
    st.stop()

st.video(load_bytes(str(VIDEO)), format="video/mp4")

st.markdown(
    "跟著畫面唱：正在唱的音會亮起來，唱過的音符和歌詞會由左到右變成橘色。"
    "下方預告的是接下來要唱的那一行，遇到反覆或 D.S. 時會直接顯示要跳去的地方。"
)

if SCORE is not None:
    with st.expander("📄 完整簡譜"):
        st.image(load_bytes(str(SCORE)), width="stretch")

col1, col2 = st.columns(2)
col1.download_button("⬇️ 下載影片（MP4）", load_bytes(str(VIDEO)),
                     file_name="雨傘情_動態曲譜_伴奏.mp4", mime="video/mp4", width="stretch")
if SCORE is not None:
    col2.download_button("⬇️ 下載簡譜（PNG）", load_bytes(str(SCORE)),
                         file_name="雨傘情_數位簡譜.png", mime="image/png", width="stretch")
