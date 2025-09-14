import streamlit as st
import streamlit.components.v1 as components

def render_why_us():
    """Render the Why Choose Us section with animated list items"""

    why_us = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Why Choose Us</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      :root {
        --primary: #3b82f6;
        --success: #16a34a;
        --accent: #25d366;
        --warning: #f59e0b;
        --bg-dark: #0a2342;
        --text-light: #f4f7fb;
        --muted: #cbd5e1;
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
      ul {
        list-style: none;
        padding: 0;
        margin: 0;
        display: grid;
        gap: 1rem;
      }
      li {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 0.8rem 1rem;
        border-radius: 12px;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 0.6s forwards;
      }
      li:nth-child(1) { animation-delay: 0.2s; }
      li:nth-child(2) { animation-delay: 0.4s; }
      li:nth-child(3) { animation-delay: 0.6s; }
      li:nth-child(4) { animation-delay: 0.8s; }
      li:nth-child(5) { animation-delay: 1s; }
      @keyframes fadeUp {
        to { opacity: 1; transform: translateY(0); }
      }
      .icon {
        flex-shrink: 0;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
        color: white;
      }
      .success { background: var(--success); }
      .primary { background: var(--primary); }
      .accent { background: var(--accent); }
      .warning { background: var(--warning); }
      strong {
        font-weight: 600;
      }
    </style>
    </head>
    <body>

    <section>
      <h2>✅ Why Choose Us</h2>
      <ul>
        <li>
          <span class="icon success">💰</span>
          <div><strong>Lowest Fee:</strong> Only 2% service charge - best in market</div>
        </li>
        <li>
          <span class="icon primary">⚡</span>
          <div><strong>Lightning Fast:</strong> Cash in your hands within minutes</div>
        </li>
        <li>
          <span class="icon accent">🕒</span>
          <div><strong>24/7 Service:</strong> Available round the clock, even holidays</div>
        </li>
        <li>
          <span class="icon warning">🔒</span>
          <div><strong>100% Secure:</strong> Bank-grade encryption and security</div>
        </li>
        <li>
          <span class="icon success">⭐</span>
          <div><strong>Trusted by 5000+:</strong> Customers across Hyderabad</div>
        </li>
      </ul>
    </section>

    </body>
    </html>
    """

    components.html(why_us, height=600, width="100%", scrolling=False)
