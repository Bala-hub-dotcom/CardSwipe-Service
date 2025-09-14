import streamlit.components.v1 as components

def render_privacy():
    """Render Privacy Policy section without full HTML doc wrapper"""

    privacy_html = """
    <style>
      .privacy-section {
        max-width: 900px;
        margin: auto;
        padding: 2rem 1rem;
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: #f4f7fb;
        line-height: 1.6;
      }
      .privacy-section h2 {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #38bdf8;
        text-align: center;
      }
      .privacy-section h3 {
        margin-top: 1.5rem;
        color: #38bdf8;
      }
      .privacy-section p {
        margin-bottom: 1rem;
        color: #cbd5e1;
      }
      .privacy-section ul {
        margin-left: 1.2rem;
        color: #cbd5e1;
      }
    </style>

    <section class="privacy-section" id="privacy">
      <h2>🔒 Privacy Policy</h2>
      <p>Your privacy is important to us. This policy explains how we collect, use, and protect your information.</p>

      <h3>1. Information We Collect</h3>
      <p>We may collect your name, contact details, and transaction information when you use our services.</p>

      <h3>2. How We Use Your Information</h3>
      <ul>
        <li>To process transactions and provide services</li>
        <li>To communicate with you regarding your transactions</li>
        <li>To comply with legal and regulatory requirements</li>
      </ul>

      <h3>3. Data Security</h3>
      <p>We use bank-grade encryption and secure systems to protect your data. We do not store your credit card details.</p>

      <h3>4. Sharing of Information</h3>
      <p>We do not sell or rent your personal information. We may share it with banks or payment processors only to complete your transactions.</p>

      <h3>5. Policy Updates</h3>
      <p>We may update this policy from time to time. Changes will be posted on this page with the updated date.</p>
    </section>
    """

    components.html(privacy_html, height=800, width="100%", scrolling=True)