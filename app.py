from pathlib import Path
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
        "description": "Dot blot解析・最適化用のWebアプリ",
        "url": "https://dot-blot-wpexuj78a34vxowmk9bdnk.streamlit.app/",
        "button": "OPEN",
        "icon": "🧪",
    },
    {
        "title": "Dot Blot 最適化ツール speed up ver.",
        "subtitle": "Speed-Up Version",
        "description": "処理速度を改善したDot blot最適化ツール",
        "url": "https://dot-blot-speed-up-ver-fxnzj3qjfjqxgtfcrmbdwc.streamlit.app/",
        "button": "OPEN",
        "icon": "⚡",
    },
    {
        "title": "qPCR 最適化ツール",
        "subtitle": "Streamlit Application",
        "description": "qPCR解析・最適化用のWebアプリ",
        "url": "https://cfnamyopjngksph65sendu.streamlit.app/",
        "button": "OPEN",
        "icon": "📈",
    },
    {
        "title": "トロンボーンパンチ",
        "subtitle": "Game",
        "description": "ブラウザで遊べるオリジナルゲーム",
        "url": "https://pickles-deth.github.io/trombonepumti/",
        "button": "PLAY",
        "icon": "🎺",
    },
]

# Portable ZIP を GitHub Releases 等へ置いた後、
# 実際のダウンロードURLへ変更してください。
PORTABLE_DOWNLOAD_URL = "https://YOUR-DOWNLOAD-LINK-HERE"

# ============================================================
# CSS
# ============================================================

css_path = Path(__file__).with_name("style.css")
if not css_path.exists():
    st.error("style.css が見つかりません。app.py と同じ階層に置いてください。")
    st.stop()

st.markdown(
    "<style>" + css_path.read_text(encoding="utf-8") + "</style>",
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================

with st.container(key="hero"):
    st.caption("RESEARCH SOFTWARE DESKTOP")
    st.title("Research App Launcher")
    st.write(
        "研究・解析・ゲーム用に作成したアプリを、ひとつのデスクトップから"
        "起動するためのポータルです。Webアプリ4種と、Windows用 "
        "Nuclear Volume Analyzer をまとめています。"
    )

st.markdown("## Applications")

# ============================================================
# APP CARDS
# ============================================================

def app_card(app, key):
    with st.container(key=key):
        st.markdown(f"### {app['icon']} {app['title']}")
        st.caption(app["subtitle"])
        st.write(app["description"])
        st.link_button(
            app["button"],
            app["url"],
            use_container_width=True,
        )

left, right = st.columns(2, gap="large")

with left:
    app_card(APPS[0], "card_dotblot")
    app_card(APPS[2], "card_qpcr")

with right:
    app_card(APPS[1], "card_dotblot_speed")
    app_card(APPS[3], "card_trombone")

# ============================================================
# WINDOWS APP
# ============================================================

st.markdown("## Windows Application")

with st.container(key="card_nuclear"):
    st.markdown("### 💿 Nuclear Volume Analyzer")
    st.caption("Windows Portable Edition")
    st.write(
        "Nuclear Volume Axial Edge AERO と "
        "Nuclear Volume Axial Edge + DAPI – Light Aero を収録したWindows版です。"
    )
    st.info(
        "Python / Anaconda / pip の知識は不要です。"
        "ZIPを展開し、STARTファイルをダブルクリックして起動します。"
    )

    if PORTABLE_DOWNLOAD_URL.startswith("https://YOUR-"):
        st.button(
            "DOWNLOAD URL 未設定",
            disabled=True,
            use_container_width=True,
        )
        st.caption(
            "PORTABLE_DOWNLOAD_URL を、完成したPortable ZIPのURLへ変更してください。"
        )
    else:
        st.link_button(
            "DOWNLOAD / INSTALL",
            PORTABLE_DOWNLOAD_URL,
            use_container_width=True,
        )

st.caption("Research Desktop • Frutiger Aero Edition")
