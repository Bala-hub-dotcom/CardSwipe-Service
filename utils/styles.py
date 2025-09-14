import streamlit as st

def load_css():
    """Load all CSS styles"""
    st.markdown("""
    <style>
    :root {
        --primary: #0052CC;
        --primary-2: #003d99;
        --success: #36B37E;
        --warning: #ff6b35;
        --accent: #7F56D9;
        --neutral-0: #ffffff;
        --neutral-5: #FDFDFE;
        --neutral-10: #FAFBFC;
        --neutral-20: #F4F5F7;
        --neutral-40: #CDD2D7;
        --neutral-70: #42526E;
        --neutral-90: #091E42;
        --shadow-1: 0 2px 8px rgba(0,0,0,0.08);
        --shadow-2: 0 8px 24px rgba(0,0,0,0.12);
        --shadow-3: 0 16px 40px rgba(0,0,0,0.15);
    }

    * { 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif; 
        box-sizing: border-box;
    }
    html, body, [data-testid="stAppViewContainer"] { 
        background: var(--neutral-10); 
        scroll-behavior: smooth;
    }

    /* LOADING ANIMATION */
    @keyframes shimmer {
        0% { background-position: -200px 0; }
        100% { background-position: calc(200px + 100%) 0; }
    }

    /* SCROLL PROGRESS BAR */
    #scroll-progress {
        position: fixed; top: 0; left: 0; height: 4px;
        width: 0; background: linear-gradient(90deg, var(--primary), #2dd4bf, #22c55e, var(--accent));
        z-index: 2000; box-shadow: 0 2px 12px rgba(0,82,204,0.4);
        transition: width 0.1s linear;
    }

    /* PARTICLE BACKGROUND */
    .particles {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: -1; overflow: hidden;
    }
    .particle {
        position: absolute; width: 4px; height: 4px; background: var(--primary);
        border-radius: 50%; opacity: 0.1;
        animation: float-particle 20s infinite linear;
    }
    @keyframes float-particle {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 0.1; }
        90% { opacity: 0.1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }

    /* ENHANCED NAVBAR */
    .navbar {
        position: sticky; top: 0; z-index: 1000;
        backdrop-filter: saturate(180%) blur(20px);
        background: rgba(255,255,255,0.85);
        padding: 0.75rem 0; margin-bottom: 0;
        border-bottom: 1px solid var(--neutral-20);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .navbar.scrolled {
        background: rgba(255,255,255,0.98);
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transform: translateY(0);
    }
    .navbar-content {
        max-width: 1200px; margin: 0 auto;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 1.5rem;
    }
    .navbar-brand {
        font-size: 1.3rem; font-weight: 800; color: var(--primary);
        text-decoration: none; display: flex; align-items: center; gap: 0.6rem;
        letter-spacing: -0.02em; transition: transform 0.3s ease;
    }
    .navbar-brand:hover { transform: scale(1.05); }
    .brand-gradient {
        background: linear-gradient(90deg, var(--primary) 0%, #22c55e 50%, var(--accent) 100%);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-shift 3s ease-in-out infinite;
    }
    @keyframes gradient-shift {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(20deg); }
    }
    .navbar-nav {
        display: flex; gap: 0.5rem; align-items: center;
        flex-wrap: wrap; justify-content: center;
    }
    .nav-link {
        color: var(--neutral-70); text-decoration: none; 
        font-weight: 600; padding: 0.5rem 0.8rem; border-radius: 12px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
        white-space: nowrap; font-size: 0.9rem;
        position: relative; overflow: hidden;
    }
    .nav-link::before {
        content: ''; position: absolute; top: 0; left: -100%;
        width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s ease;
    }
    .nav-link:hover::before { left: 100%; }
    .nav-link:hover {
        color: var(--primary); background: var(--neutral-10);
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 4px 12px rgba(0,82,204,0.15);
    }
    .nav-link.active {
        color: white; background: linear-gradient(135deg, var(--primary), var(--primary-2));
        box-shadow: 0 6px 20px rgba(0,82,204,0.3);
        transform: translateY(-1px);
    }
    .nav-contact {
        background: linear-gradient(135deg, var(--success), #22c55e);
        color: white !important;
        padding: 0.6rem 1.2rem; border-radius: 12px;
        font-weight: 700; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 0.9rem; box-shadow: 0 6px 20px rgba(34,197,94,0.3);
        position: relative; overflow: hidden;
    }
    .nav-contact::after {
        content: ''; position: absolute; top: 50%; left: 50%;
        width: 0; height: 0; background: rgba(255,255,255,0.3);
        border-radius: 50%; transition: all 0.3s ease;
        transform: translate(-50%, -50%);
    }
    .nav-contact:hover::after { width: 300px; height: 300px; }
    .nav-contact:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 25px rgba(34,197,94,0.4);
    }

    /* HERO SECTION WITH ADVANCED EFFECTS */
    .hero-wrap {
        position: relative; margin: 1rem auto 2rem auto; max-width: 1200px;
        padding: 0 1.5rem;
    }
    .hero-section {
        background: 
            radial-gradient(1200px 300px at 20% -20%, rgba(34,197,94,0.15), transparent 50%),
            radial-gradient(1200px 300px at 80% 120%, rgba(0,82,204,0.15), transparent 50%),
            linear-gradient(135deg, var(--primary) 0%, var(--primary-2) 100%);
        color: white; padding: 3rem; border-radius: 20px;
        box-shadow: var(--shadow-3);
        overflow: hidden; position: relative; isolation: isolate;
        animation: hero-entrance 1s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    @keyframes hero-entrance {
        0% { opacity: 0; transform: translateY(30px) scale(0.95); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    .hero-glow {
        position: absolute; inset: -50% -20% auto auto; width: 80vw; height: 80vw; 
        background: radial-gradient(circle, rgba(127,86,217,0.25), transparent 40%);
        filter: blur(60px); z-index: 0; transform: translate3d(0,0,0);
        animation: glow-pulse 4s ease-in-out infinite;
    }
    @keyframes glow-pulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.1); }
    }
    .hero-grid {
        position: absolute; inset: -10% 0 0 0; opacity: 0.1; z-index: 0;
        background-image: 
            linear-gradient(rgba(255,255,255,0.15) 1px, transparent 1px), 
            linear-gradient(90deg, rgba(255,255,255,0.15) 1px, transparent 1px);
        background-size: 30px 30px;
        animation: grid-move 20s linear infinite;
    }
    @keyframes grid-move {
        0% { transform: translate(0, 0); }
        100% { transform: translate(30px, 30px); }
    }
    .hero-content { position: relative; z-index: 1; }
    .hero-title {
        margin: 0; font-size: 3rem; font-weight: 900; letter-spacing: -0.03em;
        line-height: 1.1; animation: title-reveal 1.2s cubic-bezier(0.4, 0, 0.2, 1) 0.3s both;
    }
    @keyframes title-reveal {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .hero-subtitle {
        margin: 0.5rem 0 1rem 0; font-size: 1.5rem; font-weight: 700; opacity: 0.95;
        animation: subtitle-reveal 1.2s cubic-bezier(0.4, 0, 0.2, 1) 0.5s both;
    }
    @keyframes subtitle-reveal {
        0% { opacity: 0; transform: translateX(-20px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    .hero-points {
        font-size: 1.1rem; margin: 1rem 0; font-weight: 600; opacity: 0.96;
        animation: points-reveal 1.2s cubic-bezier(0.4, 0, 0.2, 1) 0.7s both;
    }
    @keyframes points-reveal {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .cta-row { 
        display: flex; align-items: center; gap: 1rem; margin-top: 1.5rem; flex-wrap: wrap;
        animation: cta-reveal 1.2s cubic-bezier(0.4, 0, 0.2, 1) 0.9s both;
    }
    @keyframes cta-reveal {
        0% { opacity: 0; transform: scale(0.9); }
        100% { opacity: 1; transform: scale(1); }
    }
    .cta-pill {
        display: inline-flex; align-items: center; gap: 0.6rem; 
        background: rgba(255,255,255,0.15); padding: 0.6rem 1rem; border-radius: 999px;
        font-weight: 700; letter-spacing: 0.5px; backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .cta-pill:hover {
        background: rgba(255,255,255,0.25);
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .badge-chip {
        display: inline-flex; align-items: center; gap: 0.4rem; 
        background: rgba(255,255,255,0.12); padding: 0.4rem 0.8rem; border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.2); font-weight: 700; font-size: 0.85rem;
        animation: badge-float 3s ease-in-out infinite;
    }
    @keyframes badge-float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
    }
    .hero-illustration {
        border-radius: 16px; overflow: hidden;
        background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 25px 60px rgba(0,0,0,0.3);
        transform-style: preserve-3d; 
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: image-entrance 1.5s cubic-bezier(0.4, 0, 0.2, 1) 1.1s both;
    }
    @keyframes image-entrance {
        0% { opacity: 0; transform: perspective(1000px) rotateY(20deg) translateX(50px); }
        100% { opacity: 1; transform: perspective(1000px) rotateY(0deg) translateX(0); }
    }
    .hero-illustration:hover { 
        transform: perspective(1000px) rotateX(5deg) rotateY(-5deg) translateY(-5px) scale(1.02);
        box-shadow: 0 35px 80px rgba(0,0,0,0.4);
    }

    /* ENHANCED CARDS WITH MICRO-INTERACTIONS */
    .service-card, .feature-card {
        background: white; padding: 1.5rem; border-radius: 16px;
        box-shadow: var(--shadow-1);
        border: 1px solid var(--neutral-20);
        margin-bottom: 1.5rem; 
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative; overflow: hidden;
        transform: translateY(0);
    }
    .service-card::before, .feature-card::before {
        content: ""; position: absolute; inset: 0; pointer-events: none;
        background: radial-gradient(600px 200px at var(--mx, 50%) var(--my, 50%), rgba(0,82,204,0.15), transparent 60%);
        opacity: 0; transition: opacity 0.4s ease;
    }
    .service-card:hover::before, .feature-card:hover::before { opacity: 1; }
    .service-card:hover, .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        border-color: rgba(0,82,204,0.3);
    }
    .service-card h4, .feature-card h4 { 
        margin: 0 0 0.5rem 0; 
        transition: color 0.3s ease;
    }
    .service-card:hover h4, .feature-card:hover h4 { color: var(--primary); }
    .service-card p, .feature-card p { 
        margin: 0; color: var(--neutral-70); 
        transition: color 0.3s ease;
    }

    /* SCROLL REVEAL ANIMATIONS */
    .reveal { 
        opacity: 0; 
        transform: translateY(30px) scale(0.95); 
        transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .reveal.visible { 
        opacity: 1; 
        transform: translateY(0) scale(1); 
    }
    .reveal-left {
        opacity: 0; 
        transform: translateX(-50px);
        transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .reveal-left.visible {
        opacity: 1;
        transform: translateX(0);
    }
    .reveal-right {
        opacity: 0; 
        transform: translateX(50px);
        transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .reveal-right.visible {
        opacity: 1;
        transform: translateX(0);
    }

    /* FLOATING ANIMATIONS */
    @keyframes float { 
        0%, 100% { transform: translateY(0) rotate(0deg); } 
        33% { transform: translateY(-8px) rotate(1deg); }
        66% { transform: translateY(-4px) rotate(-1deg); }
    }
    .floating-img { animation: float 4s ease-in-out infinite; }

    /* ENHANCED CONTACT BUTTONS */
    .contact-btn {
        display: inline-block; padding: 14px 28px; margin: 10px;
        background: linear-gradient(135deg, var(--success), #22c55e); 
        color: white; text-decoration: none;
        border-radius: 12px; font-weight: 700; 
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 25px rgba(34,197,94,0.3); 
        position: relative; overflow: hidden;
        transform: translateY(0);
    }
    .contact-btn::before {
        content: ''; position: absolute; top: 0; left: -100%;
        width: 100%; height: 100%; 
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.6s ease;
    }
    .contact-btn:hover::before { left: 100%; }
    .contact-btn:hover { 
        transform: translateY(-3px) scale(1.05); 
        box-shadow: 0 15px 35px rgba(34,197,94,0.4); 
    }
    .contact-btn:active { 
        transform: translateY(-1px) scale(1.02); 
    }

    /* RIPPLE EFFECT */
    .ripple { position: relative; overflow: hidden; }
    .ripple::after {
        content: ''; position: absolute; top: 50%; left: 50%;
        width: 0; height: 0; border-radius: 50%;
        background: rgba(255,255,255,0.5);
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    .ripple:active::after { width: 300px; height: 300px; }

    /* STATS COUNTER */
    .stats-grid {
        display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); 
        gap: 1rem; margin-top: 1rem;
    }
    .stat-card {
        background: rgba(255,255,255,0.1); 
        border: 1px solid rgba(255,255,255,0.2); 
        border-radius: 16px; padding: 1.5rem;
        text-align: center; backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stat-card:hover {
        background: rgba(255,255,255,0.15);
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .stat-number { 
        font-size: 2rem; font-weight: 900; color: white; 
        letter-spacing: -0.02em; margin-bottom: 0.5rem;
        animation: counter-up 2s ease-out;
    }
    .stat-label { 
        color: rgba(255,255,255,0.9); font-weight: 600; font-size: 0.9rem;
    }

    /* FLOATING WHATSAPP WITH PULSE */
    .whatsapp-float {
        position: fixed; bottom: 25px; right: 25px; width: 65px; height: 65px;
        background: linear-gradient(135deg, #25d366, #20ba5a); 
        border-radius: 50px; display: flex;
        justify-content: center; align-items: center; font-size: 28px;
        box-shadow: 0 8px 25px rgba(37,211,102,0.4); z-index: 1000;
        animation: float-whatsapp 3s ease-in-out infinite;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .whatsapp-float::before {
        content: ''; position: absolute; inset: -5px;
        border: 2px solid #25d366; border-radius: 50px;
        animation: pulse-ring 2s ease-out infinite;
    }
    @keyframes pulse-ring {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(1.3); opacity: 0; }
    }
    @keyframes float-whatsapp {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(5deg); }
    }
    .whatsapp-float:hover {
        transform: scale(1.1) translateY(-5px);
        box-shadow: 0 15px 35px rgba(37,211,102,0.5);
    }
    .whatsapp-float a { color: white; text-decoration: none; }

    /* BACK TO TOP FAB */
    .back-to-top {
        position: fixed; bottom: 110px; right: 30px; width: 50px; height: 50px; 
        border-radius: 50%; background: white; 
        border: 1px solid var(--neutral-20);
        box-shadow: var(--shadow-2); display: flex; align-items: center; justify-content: center;
        font-size: 22px; color: var(--primary); z-index: 999; 
        opacity: 0; transform: translateY(20px) scale(0.8);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }
    .back-to-top.show { 
        opacity: 1; 
        transform: translateY(0) scale(1); 
    }
    .back-to-top:hover {
        background: var(--primary); color: white;
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 12px 30px rgba(0,82,204,0.3);
    }

    /* ENHANCED FOOTER */
    .footer {
        background: linear-gradient(135deg, var(--neutral-90) 0%, #0a1628 100%);
        color: white; padding: 4rem 0 1.5rem 0; margin-top: 4rem;
        position: relative; overflow: hidden;
    }
    .footer::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, var(--success), transparent);
    }
    .footer-content {
        max-width: 1200px; margin: 0 auto; padding: 0 1.5rem;
        display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem;
    }
    .footer-brand h3 { 
        color: white; margin-bottom: 1rem; font-size: 1.6rem; 
        background: linear-gradient(90deg, white, #e2e8f0);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .footer-brand p { 
        color: #a0aec0; line-height: 1.7; margin-bottom: 1.5rem; 
    }
    .footer-contact { 
        display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.6rem; 
        color: #e2e8f0; font-size: 1.05rem; 
        transition: color 0.3s ease;
    }
    .footer-contact:hover { color: var(--success); }
    .footer-section h4 {
        color: white; margin-bottom: 1rem; font-size: 1.2rem;
        border-bottom: 2px solid var(--success); display: inline-block; 
        padding-bottom: 0.5rem;
    }
    .footer-section ul { list-style: none; padding: 0; margin: 0; }
    .footer-section li { margin-bottom: 0.6rem; }
    .footer-section a { 
        color: #a0aec0; text-decoration: none; 
        transition: all 0.3s ease; position: relative;
    }
    .footer-section a::after {
        content: ''; position: absolute; bottom: -2px; left: 0;
        width: 0; height: 2px; background: var(--success);
        transition: width 0.3s ease;
    }
    .footer-section a:hover::after { width: 100%; }
    .footer-section a:hover { color: var(--success); transform: translateX(5px); }
    .footer-bottom {
        border-top: 1px solid #2d3748; margin-top: 2.5rem; padding-top: 1.5rem;
        text-align: center; color: #a0aec0;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 768px) {
        .navbar-content { flex-direction: column; gap: 1rem; padding: 0 1rem; }
        .navbar-nav { gap: 0.4rem; }
        .nav-link { padding: 0.4rem 0.6rem; font-size: 0.85rem; }
        .hero-section { padding: 2rem 1.5rem; }
        .hero-title { font-size: 2.2rem; }
        .hero-subtitle { font-size: 1.3rem; }
        .stats-grid { grid-template-columns: repeat(2, 1fr); }
        .footer-content { grid-template-columns: 1fr; gap: 2rem; }
    }

    @media (max-width: 480px) {
        .navbar-nav { 
            display: grid; grid-template-columns: repeat(3, 1fr);
            gap: 0.5rem; width: 100%;
        }
        .nav-link, .nav-contact { text-align: center; font-size: 0.8rem; }
        .hero-title { font-size: 1.8rem; }
        .hero-subtitle { font-size: 1.1rem; }
        .stats-grid { grid-template-columns: 1fr; }
        .whatsapp-float { width: 55px; height: 55px; font-size: 24px; }
        .back-to-top { width: 45px; height: 45px; font-size: 18px; }
    }

    /* UTILITY CLASSES */
    .text-gradient {
        background: linear-gradient(90deg, var(--primary), var(--success));
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .blur-bg { backdrop-filter: blur(10px); }
    .glass { 
        background: rgba(255,255,255,0.1); 
        backdrop-filter: blur(10px); 
        border: 1px solid rgba(255,255,255,0.2); 
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Add JavaScript
    st.markdown("""
    <script>
    // Particle System
    function createParticles() {
        const container = document.getElementById('particles');
        if (!container) return;
        
        for (let i = 0; i < 15; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 20 + 's';
            particle.style.animationDuration = (15 + Math.random() * 10) + 's';
            container.appendChild(particle);
        }
    }

    // Smooth scrolling and navigation
    function scrollToSection(sectionId) {
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({behavior: 'smooth', block: 'start'});
            updateActiveLink(sectionId);
        }
    }

    function updateActiveLink(activeId) {
        document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
        const activeLink = document.querySelector(`[href="#${activeId}"]`);
        if (activeLink && !activeLink.classList.contains('nav-contact')) {
            activeLink.classList.add('active');
        }
    }

    // Enhanced scroll effects
    window.addEventListener('scroll', function() {
        const sections = ['home', 'how-it-works', 'services', 'why-us', 'reviews', 'faq'];
        const scrollPos = window.scrollY + 200;
        const doc = document.documentElement;
        const prog = document.getElementById('scroll-progress');
        const nav = document.getElementById('top-navbar');
        const topFab = document.getElementById('back-to-top');

        // Progress bar
        const height = doc.scrollHeight - doc.clientHeight;
        const progress = height > 0 ? (window.scrollY / height) * 100 : 0;
        if (prog) prog.style.width = progress + '%';

        // Scroll spy
        sections.forEach(section => {
            const element = document.getElementById(section);
            if (element) {
                const offsetTop = element.offsetTop;
                const height = element.offsetHeight;
                if (scrollPos >= offsetTop && scrollPos < offsetTop + height) {
                    updateActiveLink(section);
                }
            }
        });

        // Navbar effects
        if (nav) nav.classList.toggle('scrolled', window.scrollY > 10);
        
        // Back-to-top visibility
        if (topFab) topFab.classList.toggle('show', window.scrollY > 400);
    });

    // Intersection Observer for reveal animations
    const observerOptions = {
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                if (entry.target.classList.contains('stat-card')) {
                    animateCounter(entry.target);
                }
            }
        });
    }, observerOptions);

    // Counter animation
    function animateCounter(card) {
        const numEl = card.querySelector('.stat-number');
        if (!numEl || numEl.dataset.animated === '1') return;
        
        const target = parseInt(numEl.dataset.target || numEl.textContent, 10);
        const duration = 2000;
        const startTime = performance.now();
        
        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(target * easeOut);
            
            numEl.textContent = current.toLocaleString();
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                numEl.dataset.animated = '1';
            }
        }
        
        requestAnimationFrame(updateCounter);
    }

    // Mouse tracking for card effects
    document.addEventListener('mousemove', (e) => {
        document.querySelectorAll('.service-card, .feature-card').forEach(card => {
            const rect = card.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top) / rect.height) * 100;
            card.style.setProperty('--mx', x + '%');
            card.style.setProperty('--my', y + '%');
        });
    });

    // Ripple effect for buttons
    document.addEventListener('click', (e) => {
        if (e.target.closest('.ripple')) {
            const button = e.target.closest('.ripple');
            const rect = button.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute; left: ${x}px; top: ${y}px;
                width: ${size}px; height: ${size}px;
                background: rgba(255,255,255,0.5); border-radius: 50%;
                transform: scale(0); animation: ripple-effect 0.6s ease-out;
                pointer-events: none;
            `;
            
            button.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        }
    });

    // Add ripple keyframes
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple-effect {
            to { transform: scale(2); opacity: 0; }
        }
    `;
    document.head.appendChild(style);

    // Initialize everything
    window.addEventListener('DOMContentLoaded', () => {
        createParticles();
        document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => {
            observer.observe(el);
        });
        updateActiveLink('home');
    });

    // Back to top function
    function backToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Enhanced tilt effect for hero image
    function initTiltEffect() {
        const tiltElement = document.querySelector('.hero-illustration');
        if (!tiltElement) return;
        
        tiltElement.addEventListener('mousemove', (e) => {
            const rect = tiltElement.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width;
            const y = (e.clientY - rect.top) / rect.height;
            
            const tiltX = (y - 0.5) * -15;
            const tiltY = (x - 0.5) * 15;
            
            tiltElement.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateY(-5px) scale(1.02)`;
        });
        
        tiltElement.addEventListener('mouseleave', () => {
            tiltElement.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1)';
        });
    }

    // Initialize tilt effect
    setTimeout(initTiltEffect, 100);
    </script>
    """, unsafe_allow_html=True)