import streamlit as st


def load_css():
    """Inject centralized global CSS and JS for consistent SPA styling and behavior."""
    st.markdown(
        """
        <style>
        :root {
            --primary: #3b82f6;        /* blue-500 */
            --primary-600: #2563eb;    /* blue-600 */
            --success: #22c55e;        /* green-500 */
            --accent: #7c3aed;         /* violet-600 */
            --warning: #f59e0b;        /* amber-500 */
            --danger: #ef4444;         /* red-500 */
            --bg: #0b1220;             /* app dark bg */
            --text: #f4f7fb;           /* light text */
        }
        html, body, [data-testid="stAppViewContainer"] { background: var(--bg); color: var(--text); }
        /* Anchors for nav scrolling */
        .anchor { position: relative; top: -80px; height: 0; visibility: hidden; }
        /* remove extra padding at page bottom to avoid big gap after footer */
        .block-container { padding-bottom: 0 !important; }
        /* footer minimal margin-bottom to avoid gap */
        .footer { margin-bottom: 0 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # keep minimal JS (no-op placeholder)
    st.markdown("""<script>/* styles loader active */</script>""", unsafe_allow_html=True)
