import streamlit as st
import streamlit.components.v1 as components

def render_reviews():
    """Render Customer Reviews section with scroll-triggered animations and white font"""

    reviews = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Reviews</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      :root {
        --primary: #facc15;
        --text-white: #ffffff;
        --muted: #cbd5e1;
        --card-bg: rgba(255,255,255,0.05);
      }
      html, body {
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: var(--text-white);
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
      }
      section {
        max-width: 900px;
        width: 100%;
        margin: 0 auto;
        padding: 0;
      }
      h2 {
        font-size: 2rem;
        margin: 0;
        padding: 1rem 0 2rem;
        text-align: center;
        color: var(--primary);
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      h2.show {
        opacity: 1;
        transform: translateY(0);
      }
      .reviews-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 1rem;
      }
      .review-card {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1rem;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      .review-card.show {
        opacity: 1;
        transform: translateY(0);
        animation: bounce 2s ease-in-out infinite;
      }
      .review-card:nth-child(1) { transition-delay: 0.1s; }
      .review-card:nth-child(2) { transition-delay: 0.2s; }
      .review-card:nth-child(3) { transition-delay: 0.3s; }
      .review-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
        color: var(--text-white);
      }
      .stars {
        color: #ffd700;
      }
      p {
        margin: 0;
        font-style: italic;
        color: var(--text-white);
      }
      @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
      }
    </style>
    </head>
    <body>
    <section>
      <h2 id="reviews-title">⭐ Customer Reviews</h2>
      <div class="reviews-grid">
        <div class="review-card">
          <div class="review-header">
            <span class="stars">⭐⭐⭐⭐⭐</span>
            <strong>Rajesh K.</strong>
          </div>
          <p>"Got cash in 10 minutes for emergency. Super fast service!"</p>
        </div>
        <div class="review-card">
          <div class="review-header">
            <span class="stars">⭐⭐⭐⭐⭐</span>
            <strong>Priya S.</strong>
          </div>
          <p>"Lowest charges in the city. Very polite and professional staff."</p>
        </div>
        <div class="review-card">
          <div class="review-header">
            <span class="stars">⭐⭐⭐⭐⭐</span>
            <strong>Meena R.</strong>
          </div>
          <p>"They helped me at midnight during emergency. Truly 24/7!"</p>
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

      document.querySelectorAll('.review-card, #reviews-title').forEach(el => observer.observe(el));
    </script>
    </body>
    </html>
    """

    components.html(reviews, height=450, width="100%", scrolling=False)