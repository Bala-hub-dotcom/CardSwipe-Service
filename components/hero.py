import os
import streamlit as st
import streamlit.components.v1 as components
import base64

# Convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Image path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
card_img_path = os.path.join(BASE_DIR, "assets", "card_image.png")
card_img_base64 = get_base64_image(card_img_path)

def render_hero(height=550, width="100%"):
    hero_html = f"""
    <style>
    .hero-container, .hero-container * {{
        font-family: 'Segoe UI', sans-serif;
    }}

    .hero-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 5%;
        margin: 0;
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white;
        position: relative;
        overflow: hidden;
        gap: 2rem;
    }}

    .hero-text {{
        flex: 1;
        z-index: 2;
    }}

    .hero-text h3 {{
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #facc15, #fbbf24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        line-height: 1.2;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.5);
        opacity: 0;
        transform: translateY(-20px);
        animation: fadeInDown 1s forwards;
    }}

    .bullet-cards {{
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }}
    .bullet-card {{
        background: rgba(255, 255, 255, 0.1);
        border-left: 5px solid #facc15;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        font-size: 1.1rem;
        font-weight: 500;
        opacity: 0;
        transform: translateY(-50px);
        animation: dropIn 0.8s forwards, bounce 2s ease-in-out infinite;
    }}
    .bullet-card:nth-child(1) {{ animation-delay: 0.2s; }}
    .bullet-card:nth-child(2) {{ animation-delay: 0.4s; }}
    .bullet-card:nth-child(3) {{ animation-delay: 0.6s; }}
    .bullet-card:nth-child(4) {{ animation-delay: 0.8s; }}

    .hero-buttons {{
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeInUp 1s forwards;
        animation-delay: 1.2s;
    }}

    .cta-button, .whatsapp-button {{
        text-decoration: none !important;
        background-color: #facc15;
        color: black;
        padding: 14px 28px;
        border-radius: 50px;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(250, 204, 21, 0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        animation: bounce 2s ease-in-out infinite;
    }}
    .cta-button:hover, .whatsapp-button:hover {{
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(250, 191, 36, 0.45);
    }}

    .hero-image {{
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }}
    .hero-image img {{
        max-width: 550px;
        height: auto;
        border-radius: 0px;
        box-shadow: 0 0px 0px rgba(0,0,0,0.5);
    }}

    @keyframes fadeInDown {{
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fadeInUp {{
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes dropIn {{
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes bounce {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}

    @media (max-width: 992px) {{
        .hero-container {{
            flex-direction: column;
            text-align: center;
            padding: 0 5%;
            gap: 2rem;
        }}
        .hero-image img {{ max-width: 90%; }}
        .bullet-cards {{ align-items: center; }}
    }}
    </style>

    <div class="hero-container">
        <div class="hero-text">
            <h3>Spot Cash Against the Credit Card</h3>
            <div class="bullet-cards">
                <div class="bullet-card">Instant transfer to your bank account</div>
                <div class="bullet-card">Only 2% processing fee</div>
                <div class="bullet-card">Secure & encrypted transactions</div>
                <div class="bullet-card">Hassle-free and fast service</div>
            </div>
            <div class="hero-buttons">
                <a href="tel:+919505870597" class="cta-button">Get Instant Cash Now</a>
                <a href="https://wa.me/919505870597" target="_blank" class="whatsapp-button">Contact on WhatsApp</a>
            </div>
        </div>
        <div class="hero-image">
            <img src="data:image/png;base64,{card_img_base64}" alt="Credit Card">
        </div>
    </div>
    """
    components.html(hero_html, height=height, width=width, scrolling=False)