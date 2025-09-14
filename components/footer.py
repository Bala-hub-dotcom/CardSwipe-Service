import streamlit as st
import streamlit.components.v1 as components

def render_footer():
    """Render full footer with business info, nav links, social media, cards, and legal"""

    footer_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Footer</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      .footer {
          background: linear-gradient(135deg, #0f172a, #1e293b);
          color: #f8fafc;
          padding: 2rem 1rem;
          margin-top: 2rem;
          font-size: 0.9rem;
          border-top: 1px solid #334155;
          border-radius: 1rem 1rem 0 0;
          font-family: 'Segoe UI', sans-serif;
      }
      .footer-container {
          max-width: 1100px;
          margin: auto;
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
          gap: 1.5rem;
      }
      .footer h4 {
          color: #38bdf8;
          margin-bottom: 0.8rem;
          font-size: 1rem;
      }
      .footer a {
          color: #f8fafc;
          text-decoration: none;
          display: block;
          margin: 0.3rem 0;
          transition: color 0.3s ease;
      }
      .footer a:hover {
          color: #38bdf8;
      }
      .social-icons a {
          display: inline-block;
          margin-right: 0.5rem;
          font-size: 1.2rem;
      }
      .cards img {
          height: 30px;
          margin-right: 0.5rem;
          margin-top: 0.5rem;
          filter: drop-shadow(0 1px 2px rgba(0,0,0,0.4));
      }
      .footer-bottom {
          text-align: center;
          margin-top: 1.5rem;
          font-size: 0.85rem;
          border-top: 1px solid #334155;
          padding-top: 1rem;
          color: #94a3b8;
      }
    </style>
    </head>
    <body>

    <div class="footer">
      <div class="footer-container">
        <!-- Business Info -->
        <div>
          <h4>📍 Our Address</h4>
          <p>
            Sri Gayathri Traders<br>
            123 Main Street, Hyderabad, Telangana, India<br>
            📞 +91 95058 70597<br>
            🕒 Open 24/7
          </p>
        </div>

        <!-- Navigation -->
        <div>
          <h4>🔗 Quick Links</h4>
          <a href="#hero">Home</a>
          <a href="#services">Services</a>
          <a href="#why-us">Why Choose Us</a>
          <a href="#reviews">Reviews</a>
          <a href="#faq">FAQ</a>
          <a href="#contact">Contact</a>
        </div>

        <!-- Social Media -->
        <div>
          <h4>📱 Connect With Us</h4>
          <div class="social-icons">
            <a href="https://wa.me/919505870597" target="_blank">💬 WhatsApp</a>
            <a href="https://facebook.com" target="_blank">📘 Facebook</a>
            <a href="https://instagram.com" target="_blank">📸 Instagram</a>
            <a href="https://twitter.com" target="_blank">🐦 Twitter</a>
          </div>
        </div>

        <!-- Accepted Cards -->
        <div>
          <h4>💳 We Accept</h4>
          <div class="cards">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/Visa.svg" alt="Visa" onerror="this.remove()">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="MasterCard" onerror="this.remove()">
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/RuPay.svg" alt="RuPay" onerror="this.remove()">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/30/American_Express_logo.svg" alt="American Express" onerror="this.remove()">
          </div>
        </div>
      </div>

      <!-- Footer Bottom -->
      <div class="footer-bottom">
        <p>© 2025 <strong>Sri Gayathri Traders</strong> | All Rights Reserved.</p>
        <p><a href="#terms">Terms & Conditions</a> | <a href="#privacy">Privacy Policy</a></p>
        <p>⚠️ Disclaimer: We do not provide personal loans. Our service is strictly card-based spot cash withdrawal.</p>
        <p>Designed by <strong>Balachandrasekhar</strong></p>
      </div>
    </div>

    </body>
    </html>
    """

    components.html(footer_html, height=500, width="100%", scrolling=False)