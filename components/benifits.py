import streamlit as st
import streamlit.components.v1 as components
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

card_img_base64 = get_base64_image(r"D:\MyApps\CardSwipe\assets\rewards points.png")

def render_benifits():
    benifits = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Benefits</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      :root {{
        --primary: #3b82f6;
        --primary-dark: #2563eb;
        --bg-dark: #0a2342;
        --text-light: #f4f7fb;
        --muted: #cbd5e1;
        --card-bg: rgba(255,255,255,0.05);
      }}
      body {{
        margin: 0;
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: var(--text-light);
      }}
      .section {{
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 2rem;
        align-items: center;
        max-width: 1100px;
        margin: auto;
        padding: 2rem 0.5rem;
      }}
      @media (max-width: 900px) {{
        .section {{ grid-template-columns: 1fr; }}
        .image-container {{ order: -1; }}
      }}
      .content h2 {{
        font-size: 2rem;
        margin-bottom: 1.5rem;
      }}
      .content p.sub {{
        color: var(--muted);
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
      }}
      .benefits {{
        display: grid;
        grid-template-columns: 1fr;
        gap: 2rem;
      }}
      .benefit-card {{
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 0.5rem;
        border-radius: 12px;
        display: flex;
        align-items: flex-start;
        gap: 0.8rem;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 0.6s forwards;
      }}
      .benefit-card:nth-child(1) {{ animation-delay: 0.2s; }}
      .benefit-card:nth-child(2) {{ animation-delay: 0.5s; }}
      .benefit-card:nth-child(3) {{ animation-delay: 0.8s; }}
      @keyframes fadeUp {{
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      .benefit-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
      }}
      .benefit-icon {{
        font-size: 1.5rem;
        flex-shrink: 0;
      }}
      .benefit-text strong {{
        display: block;
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
      }}
      .image-container {{
        border-radius: 1px;
        overflow: hidden;
        box-shadow: 0 0px 0px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
      }}
      .image-container img {{
        width: 100%;
        height: auto;
        max-height: 550px;
        object-fit: contain;
      }}
    </style>
    </head>
    <body>

    <section class="section">
      <div class="content">
        <h2>Reward Points</h2>
        <p class="sub">Unlock instant cash from your credit card limit — enjoy rewards, zero GST, and absolutely no hidden costs.</p>
        <div class="benefits">
          <div class="benefit-card">
            <div class="benefit-icon">🎁</div>
            <div class="benefit-text">
              <strong>Earn While You Spend</strong>
              Collect valuable reward points on every transaction.
            </div>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🚫</div>
            <div class="benefit-text">
              <strong>Zero GST</strong>
              100% GST‑free for maximum savings.
            </div>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">💵</div>
            <div class="benefit-text">
              <strong>No Surprise Charges</strong>
              Transparent pricing, so you know exactly what you pay.
            </div>
          </div>
        </div>
      </div>
      <div class="image-container">
        <img src="data:image/png;base64,{card_img_base64}" alt="Credit Card Swipe Service">
      </div>
    </section>

    </body>
    </html>
    """

    components.html(benifits, height=550, width="100%", scrolling=False)