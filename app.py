
import html
import streamlit as st

st.set_page_config(
    page_title="Research App Launcher",
    page_icon="🪟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# EDIT ONLY THIS SECTION
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

# 完成した Portable ZIP を GitHub Releases 等に置き、
# そのダウンロードURLに置き換えてください。
PORTABLE_DOWNLOAD_URL = "https://YOUR-DOWNLOAD-LINK-HERE"

VERSION_TEXT = "Research Desktop v1.0"

# ============================================================
# STYLE
# ============================================================

CSS = r"""
<style>
:root{
  --deep:#042134;
  --cyan:#4ce2ff;
  --blue:#73b8ff;
  --green:#74e5ad;
}

html { scroll-behavior:smooth; }

[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(circle at 17% 16%, rgba(255,255,255,.84) 0 3.6%, transparent 3.8%),
    radial-gradient(circle at 23% 19%, rgba(255,255,255,.72) 0 5.5%, transparent 5.8%),
    radial-gradient(circle at 76% 11%, rgba(255,255,255,.70) 0 4.6%, transparent 4.9%),
    linear-gradient(180deg,#8edcff 0%,#d7f6ff 36%,#70d7d2 66%,#5fb885 100%);
  background-attachment:fixed;
}

[data-testid="stHeader"]{ background:rgba(0,0,0,0); }
#MainMenu, footer { visibility:hidden; }

.block-container{
  max-width:1200px;
  padding-top:2rem;
  padding-bottom:7rem;
}

/* startup fly-by */
.boot-lane{
  position:fixed;
  z-index:9999;
  pointer-events:none;
  top:78px;
  left:0;
  width:100vw;
  height:110px;
  overflow:hidden;
}
.boot-mascot{
  position:absolute;
  right:-310px;
  width:255px;
  height:86px;
  animation:flyAcross 2.7s cubic-bezier(.15,.75,.28,1) 1 forwards;
  filter:drop-shadow(0 12px 16px rgba(0,58,78,.22));
}
@keyframes flyAcross{
  0%   { transform:translateX(0) translateY(8px) rotate(1deg); opacity:0; }
  10%  { opacity:1; }
  85%  { opacity:1; }
  100% { transform:translateX(calc(-100vw - 350px)) translateY(-4px) rotate(-1deg); opacity:0; }
}
.boot-window{
  position:relative;
  height:82px;
  border:2px solid rgba(255,255,255,.95);
  border-radius:10px;
  background:linear-gradient(180deg,rgba(245,253,255,.92),rgba(172,229,246,.88));
  box-shadow:
    inset 0 0 0 1px rgba(25,133,169,.8),
    inset 0 3px 0 rgba(255,255,255,.75),
    0 0 0 1px rgba(6,66,92,.25);
  overflow:hidden;
}
.boot-titlebar{
  height:22px;
  background:linear-gradient(180deg,#58d5fa,#199bce 54%,#0874a9);
  border-bottom:1px solid rgba(0,63,96,.5);
}
.boot-titlebar:after{
  content:"×";
  color:white;
  position:absolute;
  right:7px;
  top:1px;
  font:bold 14px Arial;
}
.boot-scene{
  position:absolute;
  inset:24px 4px 4px;
  background:linear-gradient(#b7eeff 0 58%,#88db93 59% 100%);
  border-radius:4px;
  overflow:hidden;
}
.boot-scene:before{
  content:"";
  position:absolute;
  width:46px;height:46px;border-radius:50%;
  left:30px;top:7px;
  background:rgba(255,255,255,.82);
  box-shadow:32px 8px 0 rgba(255,255,255,.75),17px -8px 0 rgba(255,255,255,.66);
}
.boot-scene:after{
  content:"";
  position:absolute;
  width:150px;height:60px;border-radius:50%;
  right:-18px;bottom:-33px;
  background:#4dbd73;
  box-shadow:-90px 12px 0 #64cb82;
}

/* hero */
.aero-hero{
  position:relative;
  overflow:hidden;
  border:1px solid rgba(255,255,255,.8);
  border-radius:20px;
  padding:28px 30px 24px;
  background:linear-gradient(180deg,rgba(255,255,255,.74),rgba(220,249,255,.54));
  box-shadow:
    inset 0 1px 0 white,
    0 18px 42px rgba(10,74,94,.20),
    0 0 0 1px rgba(29,145,180,.28);
  backdrop-filter: blur(13px);
}
.aero-hero:after{
  content:"";
  position:absolute;
  width:250px;height:250px;border-radius:50%;
  right:-90px;top:-125px;
  background:radial-gradient(circle,rgba(255,255,255,.92),rgba(70,220,255,.14) 56%,transparent 70%);
}
.hero-kicker{
  display:inline-block;
  padding:6px 12px;
  border-radius:14px;
  border:1px solid rgba(8,115,151,.32);
  background:rgba(255,255,255,.64);
  color:#116786;
  font:700 11px/1 "Segoe UI",Arial,sans-serif;
  letter-spacing:.13em;
}
.aero-hero h1{
  color:#083b55;
  margin:13px 0 6px;
  font:800 38px/1.04 "Segoe UI",Arial,sans-serif;
  letter-spacing:-.04em;
  text-shadow:0 1px 0 white;
}
.aero-hero p{
  margin:0;
  max-width:760px;
  color:#315e72;
  font:500 15px/1.7 "Segoe UI",Arial,sans-serif;
}

.section-label{
  display:flex;
  align-items:center;
  gap:10px;
  margin:26px 2px 14px;
  color:#0a435e;
  font:800 15px "Segoe UI",Arial,sans-serif;
  text-shadow:0 1px 0 rgba(255,255,255,.9);
}
.section-label:before{
  content:"";
  width:18px;height:18px;
  border-radius:4px;
  background:linear-gradient(135deg,#eaffff,#41c6ef 55%,#0c76aa);
  border:1px solid rgba(4,70,102,.44);
  box-shadow:inset 0 1px 0 white;
}

/* card grid */
.apps-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:18px;
}
.apps-grid .win-card:last-child{
  grid-column:1 / -1;
  max-width:760px;
  width:100%;
  justify-self:center;
}

.win-card{
  overflow:hidden;
  border:1px solid rgba(8,78,111,.62);
  border-radius:11px;
  background:rgba(246,253,255,.90);
  box-shadow:
    inset 0 0 0 1px rgba(255,255,255,.90),
    0 12px 26px rgba(3,70,93,.17);
  transition:transform .18s ease, box-shadow .18s ease;
}
.win-card:hover{
  transform:translateY(-4px);
  box-shadow:
    inset 0 0 0 1px white,
    0 18px 36px rgba(3,70,93,.25),
    0 0 0 2px rgba(77,215,247,.22);
}

.win-titlebar{
  height:36px;
  display:flex;
  align-items:center;
  padding:0 8px 0 12px;
  color:white;
  background:linear-gradient(180deg,#56ccf1 0%,#168fc1 48%,#0873a5 52%,#0c6c98 100%);
  border-bottom:1px solid #075f89;
  text-shadow:0 1px 1px rgba(0,51,77,.8);
  font:700 13px "Segoe UI",Arial,sans-serif;
}
.win-controls{ margin-left:auto;display:flex;gap:4px; }
.win-control{
  width:22px;height:18px;border-radius:3px;
  display:grid;place-items:center;
  background:linear-gradient(#eefcff,#87d4ea);
  border:1px solid rgba(3,64,93,.75);
  color:#16465d;
  font:bold 11px Arial;
  text-shadow:none;
  box-shadow:inset 0 1px 0 white;
}
.win-control.close{
  background:linear-gradient(#ffd8cb,#ef6b49);
  color:white;
}

.win-body{
  padding:18px;
  min-height:158px;
  background:
    linear-gradient(180deg,rgba(255,255,255,.93),rgba(225,246,251,.82)),
    repeating-linear-gradient(0deg,transparent 0 26px,rgba(32,124,155,.035) 27px);
}
.app-row{
  display:flex;
  gap:16px;
  align-items:flex-start;
}
.app-icon{
  flex:0 0 auto;
  width:60px;height:60px;
  border-radius:14px;
  display:grid;
  place-items:center;
  border:1px solid rgba(8,86,115,.36);
  background:linear-gradient(145deg,#ffffff,#b9eff9 47%,#57bfdc);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.95),0 7px 13px rgba(10,88,111,.15);
  font-size:30px;
}
.app-title{
  color:#123f54;
  font:800 18px/1.15 "Segoe UI",Arial,sans-serif;
  margin-bottom:4px;
}
.app-subtitle{
  color:#2d7894;
  font:700 11px "Segoe UI",Arial,sans-serif;
  letter-spacing:.07em;
  text-transform:uppercase;
}
.app-desc{
  color:#4a6572;
  font:500 13px/1.55 "Segoe UI",Arial,sans-serif;
  margin-top:10px;
}

.win-bottom{
  display:flex;
  justify-content:flex-end;
  gap:8px;
  margin-top:16px;
  padding-top:12px;
  border-top:1px solid rgba(31,103,129,.16);
}
.aero-btn{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-width:105px;
  padding:8px 18px;
  border-radius:7px;
  border:1px solid #176985;
  background:linear-gradient(180deg,#effeff 0%,#9beafa 42%,#35b9df 48%,#1b8fb8 100%);
  box-shadow:inset 0 1px 0 white,0 2px 4px rgba(0,70,99,.18);
  color:#063a50 !important;
  text-decoration:none !important;
  font:800 12px "Segoe UI",Arial,sans-serif;
  letter-spacing:.06em;
  text-shadow:0 1px 0 rgba(255,255,255,.8);
  transition:filter .16s ease,transform .16s ease;
}
.aero-btn:hover{
  filter:brightness(1.08);
  transform:translateY(-1px);
}
.aero-btn:active{ transform:translateY(1px); }

/* installer */
.installer-wrap{
  margin-top:28px;
  border-radius:13px;
  overflow:hidden;
  border:1px solid rgba(7,74,105,.7);
  background:#f4fbfd;
  box-shadow:0 18px 38px rgba(3,70,93,.20);
}
.installer-title{
  padding:10px 13px;
  color:white;
  background:linear-gradient(#56cdf2,#168fc0 50%,#086d9e 52%,#075d88);
  font:700 14px "Segoe UI",Arial,sans-serif;
  text-shadow:0 1px 1px rgba(0,0,0,.45);
}
.installer-content{
  display:grid;
  grid-template-columns:90px 1fr;
  gap:20px;
  padding:24px;
  background:linear-gradient(#ffffff,#eaf8fb);
}
.install-disc{
  width:78px;height:78px;border-radius:50%;
  background:
    radial-gradient(circle at center,#f8ffff 0 8%,#2fa6dd 9% 20%,#dffaff 21% 31%,#51cdea 32% 44%,#f7ffff 45% 52%,#7bd96f 53% 70%,#3ba454 71%);
  border:1px solid rgba(7,80,107,.32);
  box-shadow:0 7px 14px rgba(2,67,89,.18),inset 0 2px 0 white;
}
.install-title{
  font:800 21px "Segoe UI",Arial,sans-serif;
  color:#153e50;
}
.install-text{
  font:500 13px/1.7 "Segoe UI",Arial,sans-serif;
  color:#4d6672;
  margin-top:7px;
}
.install-note{
  margin-top:14px;
  padding:10px 12px;
  border-radius:6px;
  background:#fffce3;
  border:1px solid #dbc96b;
  color:#665b20;
  font:600 12px/1.5 "Segoe UI",Arial,sans-serif;
}

/* fake taskbar */
.fake-taskbar{
  position:fixed;
  z-index:999;
  left:0;right:0;bottom:0;
  height:46px;
  display:flex;align-items:center;
  padding:0 14px;
  background:linear-gradient(180deg,rgba(31,164,215,.92),rgba(7,88,133,.95));
  border-top:1px solid rgba(255,255,255,.75);
  box-shadow:0 -2px 12px rgba(0,53,83,.25);
  backdrop-filter:blur(10px);
}
.start-button{
  padding:7px 15px 7px 11px;
  border-radius:19px;
  color:white;
  font:800 13px "Segoe UI",Arial,sans-serif;
  background:linear-gradient(#8de992,#33ac55 52%,#18843c 55%,#11692f);
  border:1px solid #0e642d;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.85),0 1px 2px rgba(0,0,0,.22);
  text-shadow:0 1px 1px rgba(0,0,0,.5);
}
.task-title{
  margin-left:10px;
  padding:6px 13px;
  min-width:200px;
  border:1px solid rgba(2,62,94,.6);
  border-radius:4px;
  background:linear-gradient(rgba(255,255,255,.30),rgba(255,255,255,.10));
  color:white;
  font:600 12px "Segoe UI",Arial,sans-serif;
}
.task-clock{
  margin-left:auto;
  color:#e8fbff;
  font:600 11px "Segoe UI",Arial,sans-serif;
}

@media(max-width:760px){
  .apps-grid{grid-template-columns:1fr;}
  .apps-grid .win-card:last-child{
    grid-column:auto;
    max-width:none;
  }
  .aero-hero h1{font-size:29px;}
  .installer-content{grid-template-columns:1fr;}
  .boot-lane{display:none;}
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# Startup animation
st.markdown("""
<div class="boot-lane" aria-hidden="true">
  <div class="boot-mascot">
    <div class="boot-window">
      <div class="boot-titlebar"></div>
      <div class="boot-scene"></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="aero-hero">
  <div class="hero-kicker">RESEARCH SOFTWARE DESKTOP</div>
  <h1>Research App Launcher</h1>
  <p>
    研究・解析・ゲーム用に作成したアプリを、ひとつのデスクトップから起動するためのポータルです。
    Webアプリ4種と、Windows用 Nuclear Volume Analyzer をまとめています。
  </p>
</div>
<div class="section-label">Applications</div>
""", unsafe_allow_html=True)

cards = []

for app in APPS:
    title = html.escape(app["title"])
    subtitle = html.escape(app["subtitle"])
    desc = html.escape(app["description"])
    url = html.escape(app["url"], quote=True)
    btn = html.escape(app["button"])
    icon = html.escape(app["icon"])

    target = "" if url.startswith("#") else ' target="_blank" rel="noopener noreferrer"'

    cards.append(
        f"""
        <div class="win-card">
          <div class="win-titlebar">
            {title}
            <div class="win-controls">
              <div class="win-control">—</div>
              <div class="win-control">□</div>
              <div class="win-control close">×</div>
            </div>
          </div>

          <div class="win-body">
            <div class="app-row">
              <div class="app-icon">{icon}</div>
              <div>
                <div class="app-title">{title}</div>
                <div class="app-subtitle">{subtitle}</div>
                <div class="app-desc">{desc}</div>
              </div>
            </div>

            <div class="win-bottom">
              <a class="aero-btn" href="{url}"{target}>{btn}</a>
            </div>
          </div>
        </div>
        """
    )

st.markdown(
    '<div class="apps-grid">' + "".join(cards) + "</div>",
    unsafe_allow_html=True,
)

# Installer section
safe_download = html.escape(PORTABLE_DOWNLOAD_URL, quote=True)

st.markdown(
    f"""
    <div id="installer-section" class="installer-wrap">
      <div class="installer-title">Nuclear Volume Analyzer Setup</div>

      <div class="installer-content">
        <div class="install-disc"></div>

        <div>
          <div class="install-title">Windows Portable Edition</div>

          <div class="install-text">
            <b>Nuclear Volume Axial Edge AERO</b> と
            <b>Nuclear Volume Axial Edge + DAPI – Light Aero</b>
            を収録したWindows版です。<br><br>
            Python / Anaconda / pip の知識は不要です。
            ZIPを展開し、STARTファイルをダブルクリックして起動します。
          </div>

          <div class="win-bottom"
               style="justify-content:flex-start;border-top:0;padding-top:6px;">
            <a class="aero-btn"
               href="{safe_download}"
               target="_blank"
               rel="noopener noreferrer">
              DOWNLOAD
            </a>
          </div>

          <div class="install-note">
            GitHubへ公開する前に、app.py上部の
            PORTABLE_DOWNLOAD_URL を実際の配布ZIPのURLへ変更してください。
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="fake-taskbar">
      <div class="start-button">● Start</div>
      <div class="task-title">Research App Launcher</div>
      <div class="task-clock">{html.escape(VERSION_TEXT)}</div>
    </div>
    """,
    unsafe_allow_html=True,
)
