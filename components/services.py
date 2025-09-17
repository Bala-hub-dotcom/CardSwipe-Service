import streamlit as st
import streamlit.components.v1 as components

def render_services():
    """Render Services section with animated cards, matching hero/how_it_works/benifits style"""

    services = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Services</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      :root {
        --primary: #3b82f6;
        --bg-dark: #0a2342;
        --text-light: #f4f7fb;
        --muted: #cbd5e1;
        --card-bg: rgba(255,255,255,0.05);
      }
      body {
        margin: 0;
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: var(--text-light);
      }
      section {
        padding: 3rem 1.5rem;
        max-width: 1100px;
        margin: auto;
      }
      h2 {
        font-size: 2rem;
        margin-bottom: 2rem;
        text-align: center;
      }
      .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
      }
      .service-card {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 0.6s forwards;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
      }
      .service-card:nth-child(1) { animation-delay: 0.2s; }
      .service-card:nth-child(2) { animation-delay: 0.4s; }
      .service-card:nth-child(3) { animation-delay: 0.6s; }
      .service-card:nth-child(4) { animation-delay: 0.8s; }
      .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      }
      .icon {
        font-size: 2rem;
        margin-bottom: 0.8rem;
        display: inline-block;
      }
      .service-card h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.1rem;
      }
      .service-card p {
        margin: 0;
        font-size: 0.95rem;
        color: var(--muted);
      }
      @keyframes fadeUp {
        to { opacity: 1; transform: translateY(0); }
      }
      @media (max-width: 600px) {
        h2 { font-size: 1.6rem; }
        .icon { font-size: 1.8rem; }
      }
    </style>
    </head>
    <body>

    <section>
      <h2>🛠 Our Services</h2>
      <div class="services-grid">
        <div class="service-card">
          <div class="icon">💵</div>
          <h4>Instant Spot Cash</h4>
          <p>Get immediate cash for all major credit cards with the lowest fees.</p>
        </div>
        <div class="service-card">
          <div class="icon">✈️</div>
          <h4>Travel Payments</h4>
          <p>Book flights, hotels, and travel packages with just a 2% service fee.</p>
        </div>
        <div class="service-card">
          <div class="icon">🔄</div>
          <h4>Card-to-Card Transfer</h4>
          <p>Transfer money between different credit cards seamlessly.</p>
        </div>
        <div class="service-card">
          <div class="icon">📄</div>
          <h4>Utility Payments</h4>
          <p>Pay electricity, water, and gas bills with no additional charges.</p>
        </div>
      </div>
    </section>

    </body>
    </html>
    """

    components.html(services, height=450, width="100%", scrolling=False)
