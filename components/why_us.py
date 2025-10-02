import streamlit as st
import streamlit.components.v1 as components

def render_why_us():
    """Render the Why Choose Us section with animated cards and yellow title"""

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
        --primary: #facc15;
        --success: #16a34a;
        --accent: #25d366;
        --warning: #f59e0b;
        --bg-dark: #0a2342;
        --text-light: #f4f7fb;
        --muted: #cbd5e1;
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
        max-width: 900px;
        width: 100%;
        margin: 0 auto;
        padding: 0;
      }
      h2 {
        font-size: 2rem;
        margin: 0;
        padding: 0;
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
      ul {
        list-style: none;
        padding: 0;
        margin: 2rem 0 0 0;
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
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      li.show {
        opacity: 1;
        transform: translateY(0);
        animation: bounce 2s ease-in-out infinite;
      }
      li:nth-child(1) { transition-delay: 0.1s; }
      li:nth-child(2) { transition-delay: 0.2s; }
      li:nth-child(3) { transition-delay: 0.3s; }
      li:nth-child(4) { transition-delay: 0.4s; }
      li:nth-child(5) { transition-delay: 0.5s; }
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
      @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
      }
    </style>
    </head>
    <body>
    <section>
      <h2 id="why-title">✅ Why Choose Us</h2>
      <ul>
        <li><span class="icon success">💰</span><div><strong>Lowest Fee:</strong> Only 2% service charge - best in market</div></li>
        <li><span class="icon primary">⚡</span><div><strong>Lightning Fast:</strong> Cash in your hands within minutes</div></li>
        <li><span class="icon accent">🕒</span><div><strong>24/7 Service:</strong> Available round the clock, even holidays</div></li>
        <li><span class="icon warning">🔒</span><div><strong>100% Secure:</strong> Bank-grade encryption and security</div></li>
        <li><span class="icon success">⭐</span><div><strong>Trusted by 5000+:</strong> Customers across Hyderabad</div></li>
      </ul>
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

      document.querySelectorAll('li, #why-title').forEach(el => observer.observe(el));
    </script>
    </body>
    </html>
    """

    components.html(why_us, height=550, width="100%", scrolling=False)