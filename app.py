import html
import streamlit as st

st.set_page_config(
    page_title="Research App Launcher",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# APP SETTINGS
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

# Replace this after uploading the portable ZIP somewhere.
PORTABLE_DOWNLOAD_URL = "https://YOUR-DOWNLOAD-LINK-HERE"
VERSION_TEXT = "Research Desktop v1.2"

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>
html { scroll-behavior: smooth; }

[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(circle at 8% 17%, rgba(255,255,255,.74) 0 4%, transparent 4.2%),
    radial-gradient(circle at 80% 11%, rgba(255,255,255,.63) 0 5%, transparent 5.2%),
    linear-gradient(180deg,#8fdcff 0%,#d9f7ff 37%,#73dad2 67%,#5cbb86 100%);
  background-attachment: fixed;
}

[data-testid="stHeader"] { background: rgba(0,0,0,0); }
#MainMenu, footer { visibility: hidden; }

.block-container{
  max-width: 1200px;
  padding-top: 2rem;
  padding-bottom: 7rem;
}

/* Startup bubbles */
.bubble-stage{
  position: fixed;
  inset: 0;
  z-index: 9999;
  overflow: hidden;
  pointer-events: none;
  animation: bubbleStageOut 4.2s ease forwards;
}
