from pathlib import Path
import html
import streamlit as st

st.set_page_config(
    page_title="Research App Launcher",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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
VERSION_TEXT = "Research Desktop v1.3"

css_path = Path(__file__).with_name("style.css")
css = css_path.read_text(encoding="utf-8")
st.markdown("<style>" + css + "</style>", unsafe_allow_html=True)

bubble_html = (
    '<div class="bubble-stage">'
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
st.markdown(bubble_html, unsafe_allow_html=True)

hero_html = (
    '<div class="aero-hero">'
    '<div class="hero-kicker">RESEARCH SOFTWARE DESKTOP</div>'
    '<h1>Research App Launcher</h1>'
    '<p>研究・解析・ゲーム用に作成したアプリを、'
    'ひとつのデスクトップから起動するためのポータルです。'
    'Webアプリ4種と、Windows用 Nuclear Volume Analyzer をまとめています。</p>'
    '</div>'
    '<div class="section-label">Applications</div>'
)
st.markdown(hero_html, unsafe_allow_html=True)

cards = []

for app_item in APPS:
    title = html.escape(app_item["title"])
    subtitle = html.escape(app_item["subtitle"])
    desc = html.escape(app_item["description"])
    url = html.escape(app_item["url"], quote=True)
