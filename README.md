# 雨傘情 動態曲譜（伴奏版）

一頁式網站：播放跟唱影片，並提供影片和簡譜下載。

## 檔案

```
streamlit_app.py            主程式
requirements.txt            需要的套件（只有 streamlit）
.streamlit/config.toml      深藍色主題
media/yusanqing_accompaniment.mp4   影片（720p，約 23.7 MB）
media/yusanqing_score.png           簡譜
```

## 部署到 Streamlit Community Cloud（免費）

1. 到 <https://github.com> 註冊或登入，按右上角 **+ → New repository**。名稱例如
   `yusanqing`，選 **Public**，按 **Create repository**。
2. 在新的 repository 頁面按 **uploading an existing file**，把這個資料夾裡的東西
   （`streamlit_app.py`、`requirements.txt`、`README.md`、`media` 資料夾、`.streamlit`
   資料夾）全部拖進去，按 **Commit changes**。
   - `.streamlit` 開頭是點，Windows 檔案總管可能看不到。看不到也沒關係，只是少了深色主題。
3. 到 <https://share.streamlit.io>，用 GitHub 帳號登入，按 **Create app → Deploy a public
   app from GitHub**。
4. 選剛剛的 repository，Branch 填 `main`，Main file path 填 `streamlit_app.py`。
   App URL 可以自訂，例如 `yusanqing`，網址就會是 `https://yusanqing.streamlit.app`。
5. 按 **Deploy**，等 1–2 分鐘就完成了。

## 注意

- 網址是永久的，但免費版的 app 太久沒人開會「休眠」。有人打開時，畫面會出現
  「Yes, get this app back up!」，按下去等約 30 秒就會恢復。
- 影片和伴奏是黃乙玲〈雨傘情〉錄音的衍生作品。公開放在網路上可能涉及著作權。
  如果只想給自己或特定的人看，部署後在 app 右上角 **Share → Who can view this app**
  改成只有受邀的 email 才能看。
- 想換成原唱版：把 `雨傘情_動態曲譜_原唱.mp4` 用同樣方式壓縮到 25 MB 以下，存成
  `media/yusanqing_accompaniment.mp4` 的檔名覆蓋，或修改 `streamlit_app.py` 裡的檔名。
