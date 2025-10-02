import os
import streamlit as st
import streamlit.components.v1 as components
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
card_img_path = os.path.join(BASE_DIR, "assets", "reward_points.png")
card_img_base64 = get_base64_image(card_img_path)

def render_benifits():
    benifits = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Benefits</title>
      <style>
        :root {{
          --primary: #facc15;
          --primary-dark: #fbbf24;
          --bg-dark: #0a2342;
          --text-light: #f4f7fb;
          --muted: #cbd5e1;
          --card-bg: rgba(255,255,255,0.05);
        }}
        html, body {{
          margin: 0;
          padding: 0;
          overflow: hidden;
          font-family: 'Segoe UI', sans-serif;
          background: #0b1220;
          color: var(--text-light);
          width: 100%;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
        }}
        section {{
          display: grid;
          grid-template-columns: 60% 40%;
          gap: 2rem;
          align-items: center;
          max-width: 1100px;
          width: 100%;
          margin: 0 auto;
          padding: 0;
          height: 100%;
        }}
        @media (max-width: 900px) {{
          section {{ grid-template-columns: 1fr; }}
          .image-container {{ order: -1; }}
        }}
        .content {{
          text-align: center;
        }}
        .content h2 {{
          font-size: 2rem;
          margin-bottom: 1.5rem;
          background: linear-gradient(90deg, var(--primary), var(--primary-dark));
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          opacity: 0;
          transform: translateY(20px);
          transition: opacity 0.6s ease, transform 0.6s ease;
        }}
        .content h2.show {{
          opacity: 1;
          transform: translateY(0);
        }}
        .content p.sub {{
          color: var(--muted);
          font-size: 1.1rem;
          margin-bottom: 0.5rem;
          opacity: 0;
          transform: translateY(20px);
          transition: opacity 0.6s ease 0.2s, transform 0.6s ease 0.2s;
        }}
        .content p.sub.show {{
          opacity: 1;
          transform: translateY(0);
        }}
        .benefits {{
          display: grid;
          grid-template-columns: 1fr;
          gap: 2rem;
          justify-content: center;
        }}
        .benefit-card {{
          background: var(--card-bg);
          border: 1px solid rgba(255,255,255,0.08);
          padding: 0.5rem;
          border-radius: 12px;
          display: flex;
          align-items: flex-start;
          gap: 0.8rem;
          justify-content: center;
          text-align: left;
          opacity: 0;
          transform: translateY(20px);
          transition: opacity 0.6s ease, transform 0.6s ease;
        }}
        .benefit-card.show {{
          opacity: 1;
          transform: translateY(0);
          animation: bounce 2s ease-in-out infinite;
        }}
        .benefit-icon {{
          font-size: 1.5rem;
          flex-shrink: 0;
          animation: bounce 2s ease-in-out infinite;
        }}
        .benefit-text {{
          animation: bounce 2s ease-in-out infinite;
        }}
        .benefit-text strong {{
          display: block;
          font-size: 1.05rem;
          margin-bottom: 0.5rem;
          color: var(--primary);
        }}
        .image-container {{
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100%;
        }}
        .image-container img {{
          width: 100%;
          height: 100%;
          object-fit: contain;
          border-radius: 12px;
          box-shadow: 0 8px 20px rgba(0,0,0,0.3);
          opacity: 0;
          transform: translateY(20px);
          transition: opacity 0.6s ease 0.9s, transform 0.6s ease 0.9s;
        }}
        .image-container img.show {{
          opacity: 1;
          transform: translateY(0);
        }}
        @keyframes bounce {{
          0%, 100% {{ transform: translateY(0); }}
          50% {{ transform: translateY(-10px); }}
        }}
      </style>
    </head>
    <body>
      <section>
        <div class="content">
          <h2 id="benefit-title">Reward Points</h2>
          <p class="sub" id="benefit-sub">Unlock instant cash from your credit card limit — enjoy rewards, zero GST, and absolutely no hidden costs.</p>
          <div class="benefits">
            <div class="benefit-card" id="card1">
              <div class="benefit-icon">🎁</div>
              <div class="benefit-text">
                <strong>Earn While You Spend</strong>
                Collect valuable reward points on every transaction.
              </div>
            </div>
            <div class="benefit-card" id="card2">
              <div class="benefit-icon">🚫</div>
              <div class="benefit-text">
                <strong>Zero GST</strong>
                100% GST‑free for maximum savings.
              </div>
            </div>
            <div class="benefit-card" id="card3">
              <div class="benefit-icon">💵</div>
              <div class="benefit-text">
                <strong>No Surprise Charges</strong>
                Transparent pricing, so you know exactly what you pay.
              </div>
            </div>
          </div>
        </div>
        <div class="image-container">
          <img src="data:image/png;base64,{card_img_base64}" alt="Credit Card Swipe Service" id="benefit-img">
        </div>
      </section>
      <script>
        const observer = new IntersectionObserver(entries => {{
          entries.forEach(entry => {{
            if (entry.isIntersecting) {{
              entry.target.classList.add('show');
              observer.unobserve(entry.target);
            }}
          }});
        }}, {{ threshold: 0.2 }});

        observer.observe(document.getElementById('benefit-title'));
        observer.observe(document.getElementById('benefit-sub'));
        observer.observe(document.getElementById('card1'));
        observer.observe(document.getElementById('card2'));
        observer.observe(document.getElementById('card3'));
        observer.observe(document.getElementById('benefit-img'));
      </script>
    </body>
    </html>
    """
    components.html(benifits, height=550, width="100%", scrolling=False)