import streamlit as st
import streamlit.components.v1 as components

def render_reviews():
    """Render Customer Reviews section with animated cards"""

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
        max-width: 900px;
        margin: auto;
      }
      h2 {
        font-size: 2rem;
        margin-bottom: 2rem;
        text-align: center;
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
        animation: fadeUp 0.6s forwards;
      }
      .review-card:nth-child(1) { animation-delay: 0.2s; }
      .review-card:nth-child(2) { animation-delay: 0.4s; }
      .review-card:nth-child(3) { animation-delay: 0.6s; }
      @keyframes fadeUp {
        to { opacity: 1; transform: translateY(0); }
      }
      .review-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
      }
      .stars {
        color: #ffd700;
      }
      p {
        margin: 0;
        font-style: italic;
        color: var(--muted);
      }
    </style>
    </head>
    <body>

    <section>
      <h2>⭐ Customer Reviews</h2>
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

    </body>
    </html>
    """

    components.html(reviews, height=650, width="100%", scrolling=False)