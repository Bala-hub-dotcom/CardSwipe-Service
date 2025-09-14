import streamlit.components.v1 as components

def render_cards_marquee():
    """Render marquee of credit card logos, skipping any that fail to load, with larger responsive size"""

    marquee_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Credit Card Logos Marquee</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
      body {
        margin: 0;
        font-family: 'Inter', sans-serif;
        background: #0b1220;
        color: #f4f7fb;
      }
      section {
        padding: 2rem 0;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
      }
      .marquee {
        display: flex;
        animation: scroll 20s linear infinite;
        gap: 2rem;
        align-items: center;
      }
      .marquee img {
        height: 150px;
        width: 250px;
        max-width: 100%;
        object-fit: contain;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.4));
        transition: transform 0.3s ease;
      }
      .marquee img:hover {
        transform: scale(1.05);
      }
      @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
      }
      h2 {
        text-align: center;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
      }
      /* Responsive adjustments */
      @media (max-width: 768px) {
        .marquee img {
          height: 100px;
          width: 180px;
        }
      }
      @media (max-width: 480px) {
        .marquee img {
          height: 80px;
          width: 140px;
        }
      }
    </style>
    </head>
    <body>

    <section>
      <div class="marquee">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/Visa.svg" alt="Visa" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="MasterCard" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/30/American_Express_logo.svg" alt="American Express" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/RuPay.svg" alt="RuPay" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Diners_Club_Logo3.svg" alt="Diners Club" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Discover_Card_logo.svg" alt="Discover" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/40/JCB_logo.svg" alt="JCB" onerror="this.remove()">
        <!-- Repeat logos for seamless loop -->
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/Visa.svg" alt="Visa" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="MasterCard" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/30/American_Express_logo.svg" alt="American Express" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/RuPay.svg" alt="RuPay" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Diners_Club_Logo3.svg" alt="Diners Club" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Discover_Card_logo.svg" alt="Discover" onerror="this.remove()">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/40/JCB_logo.svg" alt="JCB" onerror="this.remove()">
      </div>
    </section>

    </body>
    </html>
    """

    components.html(marquee_html, height=200, width="100%", scrolling=False)