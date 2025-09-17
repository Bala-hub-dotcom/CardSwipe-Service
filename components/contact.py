import streamlit as st
import streamlit.components.v1 as components

def render_contact():
    """Render the Contact section with modern styling, animations, and a contact form"""

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
        --primary: #3b82f6;
        --success: #16a34a;
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
        text-align: center;
      }
      h2 {
        font-size: 2rem;
        margin-bottom: 2rem;
      }
      .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
      }
      .contact-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 0.6s forwards;
      }
      .contact-card:nth-child(1) { animation-delay: 0.2s; }
      .contact-card:nth-child(2) { animation-delay: 0.4s; }
      .contact-card:nth-child(3) { animation-delay: 0.6s; }
      .contact-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
      }
      a.contact-btn {
        display: inline-block;
        padding: 0.6rem 1.2rem;
        background: var(--primary);
        color: white;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: background 0.3s ease;
      }
      a.contact-btn:hover {
        background: #2563eb;
      }
      @keyframes fadeUp {
        to { opacity: 1; transform: translateY(0); }
      }
      .info {
        font-size: 0.95rem;
        color: var(--muted);
        margin-top: 0.5rem;
      }
      /* Contact Form */
      form {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: left;
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
        color: white;
        padding: 0.6rem 1.2rem;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s ease;
      }
      button:hover {
        background: #2563eb;
      }
    </style>
    </head>
    <body>

    <section>
      <h2>📞 Contact Us Now</h2>
      <div class="contact-grid">
        <div class="contact-card">
          <a href="tel:+919505870597" class="contact-btn">📞 Call Now</a>
          <div class="info">Speak directly with our team</div>
        </div>
        <div class="contact-card">
          <a href="https://wa.me/919505870597" class="contact-btn">💬 WhatsApp</a>
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

    </body>
    </html>
    """

    components.html(contact_html, height=900, width="100%", scrolling=False)
