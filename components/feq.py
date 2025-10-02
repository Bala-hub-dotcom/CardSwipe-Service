import streamlit as st
import streamlit.components.v1 as components

def render_faq():
    """Render FAQ section with white font, yellow heading, and scroll-triggered animations"""

    faq = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ</title>
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
      h3 {
        font-size: 1.3rem;
        margin: 2rem 0 1rem;
        color: var(--text-white);
      }
      .faq-item {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        margin-bottom: 1rem;
        overflow: hidden;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      .faq-item.show {
        opacity: 1;
        transform: translateY(0);
        animation: bounce 2s ease-in-out infinite;
      }
      .faq-item:nth-child(n) {
        transition-delay: calc(0.8s * var(--i));
      }
      .faq-question {
        padding: 1rem;
        cursor: pointer;
        font-weight: 600;
        color: var(--text-white);
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .faq-answer {
        padding: 0 1rem 1rem 1rem;
        display: none;
        color: var(--text-white);
      }
      .faq-item.active .faq-answer {
        display: block;
      }
      .faq-item.active .faq-question::after {
        content: "−";
      }
      .faq-question::after {
        content: "+";
        font-size: 1.2rem;
        color: var(--primary);
      }
      @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
      }
    </style>
    </head>
    <body>
    <section>
      <h2 id="faq-title">❓ Frequently Asked Questions</h2>

      <h3>General</h3>
      <div class="faq-item" style="--i:1"><div class="faq-question">Is this service legal?</div><div class="faq-answer">✅ Yes, 100% legitimate and licensed financial service.</div></div>
      <div class="faq-item" style="--i:2"><div class="faq-question">Which cards are accepted?</div><div class="faq-answer">All major banks – Visa, MasterCard, American Express, RuPay.</div></div>
      <div class="faq-item" style="--i:3"><div class="faq-question">Do I still earn reward points?</div><div class="faq-answer">🎁 Yes, you continue to earn your bank’s reward points on eligible transactions.</div></div>

      <h3>Payments & Fees</h3>
      <div class="faq-item" style="--i:4"><div class="faq-question">Any hidden charges?</div><div class="faq-answer">❌ No hidden fees. Flat 2% service charge only.</div></div>
      <div class="faq-item" style="--i:5"><div class="faq-question">Is GST applicable?</div><div class="faq-answer">🚫 No, our service is 100% GST‑free for maximum savings.</div></div>
      <div class="faq-item" style="--i:6"><div class="faq-question">Can I use multiple cards in one transaction?</div><div class="faq-answer">💳 Yes, you can combine multiple cards to reach your desired amount.</div></div>
      <div class="faq-item" style="--i:7"><div class="faq-question">Do you provide receipts?</div><div class="faq-answer">🧾 Yes, we provide a detailed receipt for every transaction.</div></div>

      <h3>Security & Privacy</h3>
      <div class="faq-item" style="--i:8"><div class="faq-question">Is my data secure?</div><div class="faq-answer">🔒 Absolutely. We use bank‑grade encryption and never store your card details.</div></div>
      <div class="faq-item" style="--i:9"><div class="faq-question">What documents are required?</div><div class="faq-answer">🪪 A valid government‑issued ID and your credit card are required for verification.</div></div>

      <h3>Operations & Support</h3>
      <div class="faq-item" style="--i:10"><div class="faq-question">Available at night?</div><div class="faq-answer">🕒 Yes, we operate 24/7 including weekends and public holidays.</div></div>
      <div class="faq-item" style="--i:11"><div class="faq-question">How much cash can I get?</div><div class="faq-answer">Up to your card limit. Minimum ₹1,000, Maximum ₹2,00,000.</div></div>
      <div class="faq-item" style="--i:12"><div class="faq-question">How long does the process take?</div><div class="faq-answer">⏱ Usually less than 10 minutes once your card is verified.</div></div>
      <div class="faq-item" style="--i:13"><div class="faq-question">Do you offer card‑to‑card transfers?</div><div class="faq-answer">🔄 Yes, we can transfer funds directly between credit cards.</div></div>
      <div class="faq-item" style="--i:14"><div class="faq-question">Can I pay utility bills through you?</div><div class="faq-answer">📄 Yes, we support electricity, water, gas, and other utility payments with no extra charges.</div></div>
      <div class="faq-item" style="--i:15"><div class="faq-question">Do you operate on holidays?</div><div class="faq-answer">✅ Yes, we are open 365 days a year.</div></div>
    </section>

    <script>
      document.querySelectorAll('.faq-question').forEach(q => {
        q.addEventListener('click', () => {
          const item = q.parentElement;
          item.classList.toggle('active');
        });
      });

      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('show');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.2 });

      document.querySelectorAll('.faq-item, #faq-title').forEach(el => observer.observe(el));
    </script>
    </body>
    </html>
    """

    components.html(faq, height=1300, width="100%", scrolling=False)