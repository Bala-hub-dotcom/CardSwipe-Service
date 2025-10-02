import streamlit as st
from components.header import render_header
from components.hero import render_hero
from components.how_it_works import render_how_it_works
from components.services import render_services
from components.why_us import render_why_us
from components.reviews import render_reviews
from components.contact import render_contact
from components.footer import render_footer
from components.benifits import render_benifits
from components.feq import render_faq
from components.cardsMarquee import render_cards_marquee
from components.terms import render_terms
from components.privacy import render_privacy
from components.google_map import render_google_map
from utils.styles import load_css

st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sri Gayathri Traders - Credit Card Spot Cash",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    """Main application function"""
    # Load CSS and JS for animations, particles, scroll progress
    load_css()

    # Minimal standalone render when opened as ?page=terms or ?page=privacy
    try:
        params = st.query_params
        raw = params.get('page', '')
        view = (raw[0] if isinstance(raw, list) else raw).lower()
    except Exception:
        view = ''
    if view == 'terms':
        render_terms()
        return
    if view == 'privacy':
        render_privacy()
        return
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Render components sequentially
    render_header()          # Navigation bar

    st.markdown('<div id="home" class="anchor"></div>', unsafe_allow_html=True)
    render_hero(height=550)  # Hero section with credit card image

    st.markdown('<div id="how-it-works" class="anchor"></div>', unsafe_allow_html=True)
    render_how_it_works()    # How It Works section

    render_benifits()        # Benifits section

    st.markdown('<div id="services" class="anchor"></div>', unsafe_allow_html=True)
    render_services()        # Services section

    st.markdown('<div id="why-us" class="anchor"></div>', unsafe_allow_html=True)
    render_why_us()          # Why Us section

    st.markdown('<div id="faq" class="anchor"></div>', unsafe_allow_html=True)
    render_faq()             # Reviews & FAQ section

    #st.markdown('<div id="terms" class="anchor"></div>', unsafe_allow_html=True)
    #render_terms()           # Terms section

    #st.markdown('<div id="privacy" class="anchor"></div>', unsafe_allow_html=True)
    #render_privacy()         # Conditions section

    st.markdown('<div id="reviews" class="anchor"></div>', unsafe_allow_html=True)
    render_reviews()         # Reviews & FAQ section

    st.markdown('<div id="contact" class="anchor"></div>', unsafe_allow_html=True)
    render_contact()         # Contact section

    render_cards_marquee()   # Cards Marquee section

    # Google Map component above the footer
    render_google_map()

    render_footer()          # Footer
   
   
 
    st.markdown("""
    <style>
    body { margin-bottom: 0 !important; }
    .main-container { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    .stApp { padding-bottom: 0 !important; }
    </style>
""", unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()
