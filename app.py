# APPLICATION CARDS
# IMPORTANT:
# HTML is deliberately generated without leading indentation.
# This prevents Streamlit/Markdown from displaying it as code.
# ============================================================

cards = []

for app in APPS:
    title = html.escape(app["title"])
    subtitle = html.escape(app["subtitle"])
    desc = html.escape(app["description"])
    url = html.escape(app["url"], quote=True)
    btn = html.escape(app["button"])
    icon = html.escape(app["icon"])

    target = (
        ""
        if url.startswith("#")
        else ' target="_blank" rel="noopener noreferrer"'
    )

    card = (
        '<div class="win-card">'
        '<div class="win-titlebar">'
        f'{title}'
        '<div class="win-controls">'
        '<div class="win-control">—</div>'
        '<div class="win-control">□</div>'
        '<div class="win-control close">×</div>'
        '</div>'
        '</div>'
        '<div class="win-body">'
        '<div class="app-row">'
        f'<div class="app-icon">{icon}</div>'
        '<div>'
        f'<div class="app-title">{title}</div>'
        f'<div class="app-subtitle">{subtitle}</div>'
        f'<div class="app-desc">{desc}</div>'
        '</div>'
        '</div>'
        '<div class="win-bottom">'
        f'<a class="aero-btn" href="{url}"{target}>{btn}</a>'
        '</div>'
        '</div>'
        '</div>'
    )

    cards.append(card)

st.markdown(
    '<div class="apps-grid">' + "".join(cards) + '</div>',
    unsafe_allow_html=True,
)

# ============================================================
# NUCLEAR VOLUME ANALYZER DOWNLOAD
# ============================================================

safe_download = html.escape(PORTABLE_DOWNLOAD_URL, quote=True)

installer_html = (
    '<div id="installer-section" class="installer-wrap">'
    '<div class="installer-title">Nuclear Volume Analyzer Setup</div>'
    '<div class="installer-content">'
    '<div class="install-disc"></div>'
    '<div>'
    '<div class="install-title">Windows Portable Edition</div>'
    '<div class="install-text">'
    '<b>Nuclear Volume Axial Edge AERO</b> と '
    '<b>Nuclear Volume Axial Edge + DAPI – Light Aero</b> '
    'を収録したWindows版です。<br><br>'
    'Python / Anaconda / pip の知識は不要です。'
    'ZIPを展開し、STARTファイルをダブルクリックして起動します。'
    '</div>'
    '<div class="win-bottom" '
    'style="justify-content:flex-start;border-top:0;padding-top:6px;">'
    f'<a class="aero-btn" href="{safe_download}" '
    'target="_blank" rel="noopener noreferrer">DOWNLOAD</a>'
    '</div>'
    '<div class="install-note">'
    'GitHubへ公開する前に、app.py上部の '
    '<b>PORTABLE_DOWNLOAD_URL</b> を実際の配布ZIPのURLへ変更してください。'
    '</div>'
    '</div>'
    '</div>'
    '</div>'
)

st.markdown(installer_html, unsafe_allow_html=True)

# ============================================================
# TASKBAR
# ============================================================

st.markdown(
    '<div class="fake-taskbar">'
    '<div class="start-button">● Start</div>'
    '<div class="task-title">Research App Launcher</div>'
    f'<div class="task-clock">{html.escape(VERSION_TEXT)}</div>'
    '</div>',
    unsafe_allow_html=True,
)
