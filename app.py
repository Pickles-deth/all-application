from pathlib import Path
import html
import streamlit as st

st.set_page_config(
    page_title="Research App Launcher",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# APPLICATION SETTINGS
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
    {
        "title": "Nuclear Volume Analyzer",
        "subtitle": "Windows Portable Edition",
        "description": "Edge AERO と Light Aero Accent + DAPI を収録したWindows版です。",
        "url": "#installer-section",
        "button": "INSTALL",
        "icon": "💿",
    },
]

# 完成したPortable ZIPをGitHub Releases等に置いた後、
# 実際のダウンロードURLへ変更してください。
PORTABLE_DOWNLOAD_URL = "https://YOUR-DOWNLOAD-LINK-HERE"

VERSION_TEXT = "Research Desktop v1.5"

# ============================================================
# LOAD CSS
# ============================================================

css_path = Path(__file__).with_name("style.css")

if not css_path.exists():
    st.error("style.css が見つかりません。app.py と同じGitHubフォルダに置いてください。")
    st.stop()

css = css_path.read_text(encoding="utf-8")
st.html("<style>" + css + "</style>")

# ============================================================
# STARTUP BUBBLES
# ============================================================

bubble_html = (
    '<div class="bubble-stage" aria-hidden="true">'
    '<div class="bubble b1"></div>'
    '<div class="bubble b2"></div>'
    '<div class="bubble b3"></div>'
    '<div class="bubble b4"></div>'
    '<div class="bubble b5"></div>'
    '<div class="bubble b6"></div>'
    '<div class="bubble b7"></div>'
    '<div class="bubble b8"></div>'
    '</div>'
)
st.html(bubble_html)

# ============================================================
