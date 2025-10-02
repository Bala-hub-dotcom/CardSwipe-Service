import streamlit.components.v1 as components

def render_terms():
    """Render Terms & Conditions section with animated header"""

    terms_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms & Conditions</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      html, body, section {
        margin: 0;
        padding: 0;
        overflow: hidden;
      }
      body {
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: #f4f7fb;
        line-height: 1.6;
      }
      section {
        max-width: 900px;
        margin: auto;
        padding: 2rem 1rem;
      }
      h2 {
        font-size: 2rem;
        margin-bottom: 1rem;
        text-align: center;
        background: linear-gradient(90deg, #facc15, #fbbf24);
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
      h3 {
        margin-top: 1.5rem;
        color: #38bdf8;
      }
      p {
        margin-bottom: 1rem;
        color: #cbd5e1;
      }
      ul {
        margin-left: 1.2rem;
        color: #cbd5e1;
      }
    </style>
    </head>
    <body>
    <section>
      <h2 id="terms-title">📜 Terms & Conditions</h2>
      <p>Welcome to Sri Gayathri Traders. By using our services, you agree to the following terms and conditions. Please read them carefully.</p>

      <h3>1. Service Scope</h3>
      <p>We provide credit card spot cash withdrawal, card-to-card transfers, and bill payment services. We do not offer personal loans or any form of credit issuance.</p>

      <h3>2. Eligibility</h3>
      <p>Services are available to individuals aged 18 and above with valid government-issued ID and a credit card from an accepted bank.</p>

      <h3>3. Fees & Charges</h3>
      <p>A flat 2% service fee applies to all transactions unless otherwise stated. No hidden charges are applied.</p>

      <h3>4. Transaction Limits</h3>
      <p>Minimum ₹1,000 and maximum ₹2,00,000 per transaction, subject to your card limit.</p>

      <h3>5. Liability</h3>
      <p>We are not responsible for delays or failures caused by banking systems, network issues, or force majeure events.</p>

      <h3>6. Amendments</h3>
      <p>We reserve the right to update these terms at any time. Continued use of our services constitutes acceptance of the updated terms.</p>
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

      observer.observe(document.getElementById('terms-title'));
    </script>
    </body>
    </html>
    """

    components.html(terms_html, height=800, width="100%", scrolling=False)