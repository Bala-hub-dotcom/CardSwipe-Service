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
from utils.styles import load_css

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
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Render components sequentially
    render_header()          # Navigation bar
    render_hero(height=550)  # Hero section with credit card image
    render_how_it_works()    # How It Works section
    render_benifits()        # Benifits section
    render_services()        # Services section
    render_why_us()          # Why Us section
    render_reviews()         # Reviews & FAQ section
    render_contact()         # Contact section
    render_faq()             # Reviews & FAQ section
    render_cards_marquee()   # Cards Marquee section
    render_terms()           # Terms section
    render_privacy           # Conditions section
    render_footer()          # Footer

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()