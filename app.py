from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Research App Launcher",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SETTINGS
# ============================================================

APPS = [
    {
        "title": "Dot Blot 最適化ツール",
        "subtitle": "Streamlit Application",
        "description": "Dot blot解析・最適化用のWebアプリです。",
        "url": "https://dot-blot-wpexuj78a34vxowmk9bdnk.streamlit.app/",
        "button": "OPEN",
        "icon": "🧪",
    },
    {
        "title": "Dot Blot 最適化ツール",
        "subtitle": "Speed-Up Version",
        "description": "処理速度を改善したDot blot最適化ツールです。",
        "url": "https://dot-blot-speed-up-ver-fxnzj3qjfjqxgtfcrmbdwc.streamlit.app/",
        "button": "OPEN",
        "icon": "⚡",
    },
    {
        "title": "qPCR 最適化ツール",
        "subtitle": "Streamlit Application",
        "description": "qPCR解析・最適化用のWebアプリです。",
        "url": "https://cfnamyopjngksph65sendu.streamlit.app/",
        "button": "OPEN",
        "icon": "📈",
    },
    {
        "title": "トロンボーンパンチ",
        "subtitle": "Game",
        "description": "ブラウザで遊べるオリジナルゲームです。",
        "url": "https://pickles-deth.github.io/trombonepumti/",
        "button": "PLAY",
        "icon": "🎺",
    },
]

# Nuclear Volume Analyzer の完成ZIPを GitHub Releases 等に置いた後、
# 下記を実際のURLへ変更してください。
PORTABLE_DOWNLOAD_URL = "https://YOUR-DOWNLOAD-LINK-HERE"

# ============================================================
# CSS
# ============================================================

css_path = Path(__file__).with_name("style.css")

if css_path.exists():
    css = css_path.read_text(encoding="utf-8")
    st.markdown("<style>" + css + "</style>", unsafe_allow_html=True)
else:
    st.warning("style.css が見つかりません。app.py と同じフォルダに置いてください。")

# ============================================================
# HERO
# ============================================================

with st.container(border=True):
    st.caption("RESEARCH SOFTWARE DESKTOP")
    st.title("Research App Launcher")
    st.write(
        "研究・解析・ゲーム用に作成したアプリを、ひとつのデスクトップから"
        "起動するためのポータルです。Webアプリ4種と、Windows用 "
        "Nuclear Volume Analyzer をまとめています。"
    )

st.subheader("Applications")

# ============================================================
# NATIVE STREAMLIT APP CARDS
# ============================================================

def render_app_card(app):
    with st.container(border=True):
        st.markdown(f"#### {app['icon']} {app['title']}")
        st.caption(app["subtitle"])
        st.write(app["description"])
        st.link_button(
            app["button"],
            app["url"],
            use_container_width=True,
        )

row1_left, row1_right = st.columns(2, gap="medium")
