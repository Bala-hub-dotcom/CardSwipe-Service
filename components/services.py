import streamlit as st
import streamlit.components.v1 as components

def render_services():
    """Render Services section with scroll-triggered animations and staggered loading effects"""

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
        --primary: #facc15;
        --primary-dark: #fbbf24;
        --bg-dark: #0a2342;
        --text-light: #f4f7fb;
        --muted: #cbd5e1;
        --card-bg: rgba(255,255,255,0.05);
      }
      html, body {
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: var(--text-light);
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      section {
        max-width: 1100px;
        width: 100%;
        margin: 0 auto;
        padding: 0;
      }
      h2 {
        font-size: 2rem;
        margin: 0;
        padding: 1rem 0 2rem;
        text-align: center;
        background: linear-gradient(90deg, var(--primary), var(--primary-dark));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      h2.show {
        opacity: 1;
        transform: translateY(0);
      }
      .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
      }
      .service-card {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 2rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        min-height: 250px;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      .service-card.show {
        opacity: 1;
        transform: translateY(0);
        animation: bounce 2s ease-in-out infinite;
      }
      .service-card:nth-child(1) { transition-delay: 0.2s; }
      .service-card:nth-child(2) { transition-delay: 0.4s; }
      .service-card:nth-child(3) { transition-delay: 0.6s; }
      .service-card:nth-child(4) { transition-delay: 0.8s; }
      .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      }
      .icon {
        font-size: 2.2rem;
        margin-bottom: 1rem;
        display: inline-block;
        animation: bounce 2s ease-in-out infinite;
      }
      .service-card h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.2rem;
        color: var(--primary);
      }
      .service-card p {
        margin: 0;
        font-size: 0.95rem;
        color: var(--muted);
        line-height: 1.5;
      }
      @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
      }
      @media (max-width: 600px) {
        h2 { font-size: 1.6rem; }
        .icon { font-size: 2rem; }
      }
    </style>
    </head>
    <body>
    <section>
      <h2 id="services-title">🛠 Our Services</h2>
      <div class="services-grid">
        <div class="service-card">
          <div class="icon">💵</div>
          <h4>Instant Spot Cash</h4>
          <p>Swipe your credit card and receive cash instantly. No waiting, no hassle. <br><span style="color:#facc15;">Lowest service fee guaranteed.</span></p>
        </div>
        <div class="service-card">
          <div class="icon">✈️</div>
          <h4>Travel Payments</h4>
          <p>Book flights, hotels, and packages using your card limit. <br><span style="color:#facc15;">Only 2% service fee — no hidden charges.</span></p>
        </div>
        <div class="service-card">
          <div class="icon">🔄</div>
          <h4>Card-to-Card Transfer</h4>
          <p>Move funds between credit cards with ease. <br><span style="color:#facc15;">Fast, secure, and GST-free.</span></p>
        </div>
        <div class="service-card">
          <div class="icon">📄</div>
          <h4>Utility Payments</h4>
          <p>Pay electricity, water, and gas bills using your card. <br><span style="color:#facc15;">No extra charges. Instant confirmation.</span></p>
        </div>
      </div>
    </section>
    <script>
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('show');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.2 });

      document.querySelectorAll('.service-card, #services-title').forEach(el => observer.observe(el));
    </script>
    </body>
    </html>
    """

    components.html(services, height=550, width="100%", scrolling=False)