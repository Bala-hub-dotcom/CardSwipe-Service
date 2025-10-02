import streamlit as st
import streamlit.components.v1 as components

def render_contact():
    """Render the Contact section with scroll-triggered animations and visible phone/WhatsApp routing"""

    contact_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      :root {
        --primary: #facc15;
        --text-white: #ffffff;
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
        text-align: center;
      }
      h2 {
        font-size: 2rem;
        margin: 0;
        padding: 1rem 0 2rem;
        color: var(--primary);
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      h2.show {
        opacity: 1;
        transform: translateY(0);
      }
      .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
      }
      .contact-card {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
      }
      .contact-card.show {
        opacity: 1;
        transform: translateY(0);
        animation: bounce 2s ease-in-out infinite;
      }
      .contact-card:nth-child(1) { transition-delay: 0.2s; }
      .contact-card:nth-child(2) { transition-delay: 0.4s; }
      .contact-card:nth-child(3) { transition-delay: 0.6s; }
      .contact-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
      }
      a.contact-btn {
        display: inline-block;
        padding: 0.6rem 1.2rem;
        background: var(--primary);
        color: #000;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: background 0.3s ease;
      }
      a.contact-btn:hover {
        background: #eab308;
      }
      .info {
        font-size: 0.95rem;
        color: var(--text-white);
        margin-top: 0.5rem;
      }
      form {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: left;
        color: var(--text-white);
      }
      label {
        display: block;
        margin-bottom: 0.3rem;
        font-weight: 600;
      }
      input, textarea {
        width: 100%;
        padding: 0.6rem;
        margin-bottom: 1rem;
        border: none;
        border-radius: 8px;
        font-family: inherit;
        font-size: 1rem;
      }
      input:focus, textarea:focus {
        outline: 2px solid var(--primary);
      }
      button {
        background: var(--primary);
        color: #000;
        padding: 0.6rem 1.2rem;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s ease;
      }
      button:hover {
        background: #eab308;
      }
      @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
      }
    </style>
    </head>
    <body>
    <section>
      <h2 id="contact-title">📞 Contact Us Now</h2>
      <div class="contact-grid">
        <div class="contact-card">
          <a href="tel:+919505870597" class="contact-btn">📞 Call Now</a>
          <div class="info">+91 95058 70597</div>
        </div>
        <div class="contact-card">
          <a href="https://web.whatsapp.com/send?phone=919505870597" class="contact-btn" target="_blank">💬 WhatsApp</a>
          <div class="info">Chat with us instantly</div>
        </div>
        <div class="contact-card">
          <div><strong>📍 Location:</strong> Hyderabad</div>
          <div><strong>🕒 Timing:</strong> 24/7 Open</div>
        </div>
      </div>

      <form action="mailto:youremail@example.com" method="post" enctype="text/plain">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your name" required>

        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Your email" required>

        <label for="message">Message</label>
        <textarea id="message" name="message" rows="4" placeholder="Your message" required></textarea>

        <button type="submit">Send Message</button>
      </form>
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

      document.querySelectorAll('.contact-card, #contact-title').forEach(el => observer.observe(el));
    </script>
    </body>
    </html>
    """

    components.html(contact_html, height=650, width="100%", scrolling=False)