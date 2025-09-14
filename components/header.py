import streamlit as st

def render_header():
    st.markdown("""
    <style>
    /* ---------- Navbar Styling ---------- */
    .navbar {
        position: sticky;
        top: 0;
        width: 100%;
        background: rgba(15, 32, 39, 0.95);
        backdrop-filter: blur(10px);
        z-index: 999;
        padding: 0.6rem 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Inter', sans-serif;
    }

    .navbar-brand {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        text-decoration: none;
        background: linear-gradient(90deg, #64b5f6, #1976d2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .navbar-nav {
        display: flex;
        gap: 2rem;
    }

    .navbar-nav a {
        color: #f4f7fb;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease, transform 0.3s ease;
        padding: 0.3rem 0.5rem;
    }

    .navbar-nav a:hover {
        color: #64b5f6;
        transform: translateY(-2px);
        border-bottom: 2px solid #64b5f6;
    }

    /* Scroll progress bar */
    #scroll-progress {
        position: fixed;
        top: 0;
        left: 0;
        height: 4px;
        background: linear-gradient(90deg, #64b5f6, #1976d2);
        width: 0%;
        z-index: 1000;
        transition: width 0.25s ease;
    }

    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            align-items: flex-start;
        }
        .navbar-nav {
            flex-direction: column;
            gap: 1rem;
            margin-top: 0.5rem;
        }
    }
    </style>

    <div id="scroll-progress"></div>
    <nav class="navbar">
        <a href="#" class="navbar-brand" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
            💳 Sri Gayathri Traders
        </a>
        <div class="navbar-nav">
            <a href="#home">Home</a>
            <a href="#how-it-works">How It Works</a>
            <a href="#services">Services</a>
            <a href="#why-us">Why Us</a>
            <a href="#reviews">Reviews</a>
            <a href="#faq">FAQ</a>
            <a href="tel:+919505870597">Call Now</a>
        </div>
    </nav>

    <script>
    // Scroll progress bar
    window.addEventListener('scroll', function() {
        let scrollTop = window.scrollY;
        let docHeight = document.body.scrollHeight - window.innerHeight;
        let scrollPercent = (scrollTop / docHeight) * 100;
        document.getElementById('scroll-progress').style.width = scrollPercent + '%';
    });
    </script>
    """, unsafe_allow_html=True)