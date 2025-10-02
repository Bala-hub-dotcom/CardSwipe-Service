import streamlit.components.v1 as components

def render_footer():
    """Render footer with enhanced quick links navigation and embedded chat."""

    footer_html = f"""
    <style>
    .footer {{
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: #f8fafc;
        padding: 1rem 0.5rem 1rem; /* reduced bottom padding */
        margin-top: 0.2rem;
        font-size: 0.9rem;
        border-top: 1px solid #334155;
        border-radius: 1rem 1rem 0 0;
        font-family: 'Segoe UI', sans-serif;
        position: relative;
    }}
    .footer-container {{
        max-width: 1100px;
        margin: auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1rem;
    }}
    .footer h4 {{
        color: #38bdf8;
        margin-bottom: 0.8rem;
        font-size: 1rem;
    }}
    .footer a {{
        color: #f8fafc;
        text-decoration: none;
        display: block;
        margin: 0.3rem 0;
        transition: color 0.3s ease;
        cursor: pointer;
    }}
    .footer a:hover {{ color: #38bdf8; }}
    .social-icons a {{ display: inline-block; margin-right: 0.5rem; font-size: 1.2rem; }}
    .cards img {{ height: 30px; margin-right: 0.5rem; margin-top: 0.5rem; filter: drop-shadow(0 1px 2px rgba(0,0,0,0.4)); }}
    .footer-bottom {{ text-align: center; margin-top: 1.2rem; font-size: 0.85rem; border-top: 1px solid #334155; padding-top: 1rem; color: #94a3b8; }}
    </style>

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
          <a href="#home" data-anchor="home">Home</a>
          <a href="#how-it-works" data-anchor="how-it-works">How It Works</a>
          <a href="#services" data-anchor="services">Services</a>
          <a href="#why-us" data-anchor="why-us">Why Choose Us</a>
          <a href="#reviews" data-anchor="reviews">Reviews</a>
          <a href="#faq" data-anchor="faq">FAQ</a>
          <a href="#contact" data-anchor="contact">Contact</a>
          <a href="#" data-open="terms">Terms & Conditions</a>
          <a href="#" data-open="privacy">Privacy Policy</a>
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

      <div class="footer-bottom">
        <p>© 2025 <strong>Sri Gayathri Traders</strong> | All Rights Reserved.</p>
        <p>⚠️ Disclaimer: We do not provide personal loans. Our service is strictly card-based spot cash withdrawal.</p>
        <p>Designed by <strong>Dev Solutions</strong></p>
      </div>

      <!-- ✅ Chatbot injected here -->
    </div>

    <script>
    // Footer: intercept quick link clicks to scroll parent page or open new tab for terms/privacy
    (function() {{
      function openNewTabTo(hash) {{
        try {{
          const base = window.top.location.href.split('#')[0].split('?')[0];
          window.open(base + hash, '_blank');
        }} catch (e) {{ /* ignore */ }}
      }}
      function scrollToAnchor(id) {{
        try {{
          const doc = window.top.document;
          const el = doc.getElementById(id);
          if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }} catch (e) {{ /* ignore */ }}
      }}
      document.addEventListener('click', function(e) {{
        const a1 = e.target.closest('a[data-anchor]');
        if (a1) {{ e.preventDefault(); scrollToAnchor(a1.getAttribute('data-anchor')); return; }}
        const a2 = e.target.closest('a[data-open]');
        if (a2) {{
          e.preventDefault();
          const which = a2.getAttribute('data-open');
          // open as standalone page using query parameter to let main.py render just that section
          const target = which === 'terms' ? '?page=terms' : '?page=privacy';
          openNewTabTo(target);
        }}
      }});
    }})();
    </script>
    """

    components.html(footer_html, height=450, width="100%", scrolling=False)