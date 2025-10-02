import streamlit as st
import streamlit.components.v1 as components

def render_how_it_works():
    how_it_works = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>How It Works</title>
      <style>
        :root {
          --primary: #facc15;
          --primary-dark: #fbbf24;
          --bg-dark: #0a2342;
          --text-light: #f4f7fb;
        }
        html, body {
          margin: 0;
          padding: 0;
          font-family: 'Segoe UI', sans-serif;
          background: #0b1220;
          color: var(--text-light);
          width: 100vw;
          height: 60%;
        }
        section {
          padding: 0 1.5rem;
          max-width: 1100px;
          margin: auto;
        }
        h2 {
          font-size: 2rem;
          margin: 2rem 0;
          text-align: center;
          background: linear-gradient(90deg, var(--primary), var(--primary-dark));
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
        .steps {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 1rem;
        }
        .step {
          background: linear-gradient(180deg, var(--bg-dark), #0f2e57);
          padding: 1rem 0.5rem;
          border-radius: 10px;
          box-shadow: 0 10px 30px rgba(0,0,0,0.3);
          text-align: center;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .step:hover {
          transform: translateY(-5px);
          box-shadow: 0 15px 40px rgba(0,0,0,0.5);
        }
        .step-icon {
          font-size: 3rem;
          margin-bottom: 1rem;
          display: inline-block;
          padding: 15px;
          border-radius: 50%;
          background: linear-gradient(145deg, var(--primary), var(--primary-dark));
          box-shadow: 5px 5px 15px rgba(0,0,0,0.3), -5px -5px 15px rgba(255,255,255,0.1);
          animation: bounce 2s ease-in-out infinite;
        }
        .step h3, .step p {
          opacity: 0;
          transform: translateY(15px);
          animation: bounce 2s ease-in-out infinite;
        }
        .show .step h3 {
          animation: fadeUp 0.6s forwards ease-out;
          animation-delay: 0.2s;
        }
        .show .step p {
          animation: fadeUp 0.6s forwards ease-out;
          animation-delay: 0.4s;
        }
        @keyframes fadeUp {
          to { opacity: 1; transform: translateY(0); }
        }
        @keyframes bounce {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-10px); }
        }
        .step h3 {
          position: relative;
          display: inline-block;
        }
        .step h3::after {
          content: "";
          position: absolute;
          left: 0;
          bottom: -4px;
          width: 0%;
          height: 2px;
          background-color: var(--primary);
          transition: width 0.3s ease;
        }
        .step:hover h3 {
          color: var(--primary);
        }
        .step:hover h3::after {
          width: 100%;
        }
        .step p {
          border-radius: 6px;
          padding: 4px 6px;
        }
        .step:hover p {
          color: #ffffff;
          transform: translateY(-3px);
          background-color: rgba(250, 204, 21, 0.15);
        }
        .fade-in {
          opacity: 0;
          transform: translateY(20px);
          transition: opacity 0.8s ease, transform 0.8s ease;
        }
        .fade-in.show {
          opacity: 1;
          transform: translateY(0);
        }
        .stagger > * {
          opacity: 0;
          transform: translateY(20px);
        }
        .stagger.show > * {
          animation: staggerFade 0.6s forwards;
        }
        .stagger.show > *:nth-child(1) { animation-delay: 0.1s; }
        .stagger.show > *:nth-child(2) { animation-delay: 0.3s; }
        .stagger.show > *:nth-child(3) { animation-delay: 0.5s; }
        .stagger.show > *:nth-child(4) { animation-delay: 0.7s; }
        @keyframes staggerFade {
          to { opacity: 1; transform: translateY(0); }
        }
        @media (max-width: 600px) {
          h2 { font-size: 1.6rem; }
          .step-icon { font-size: 2.5rem; padding: 12px; }
          .step h3 { font-size: 1.2rem; }
          .step p { font-size: 0.95rem; }
        }
      </style>
    </head>
    <body>
      <section>
        <h2 class="fade-in">How It Works</h2>
        <div class="steps stagger">
          <div class="step">
            <div class="step-icon">💬</div>
            <h3>Step 1: Connect with Us</h3>
            <p>Engage in person or via WhatsApp. Our team ensures a smooth, hassle-free experience.</p>
          </div>
          <div class="step">
            <div class="step-icon">🏦</div>
            <h3>Step 2: Bank Account Verification</h3>
            <p>Share your bank details securely. We deposit ₹1 to verify your account for seamless transactions.</p>
          </div>
          <div class="step">
            <div class="step-icon">💳</div>
            <h3>Step 3: Credit Card Transaction</h3>
            <p>Complete your payment via swipe or online methods. Enter the OTP securely to authorize.</p>
          </div>
          <div class="step">
            <div class="step-icon">⚡</div>
            <h3>Step 4: Instant Fund Transfer</h3>
            <p>Once verified, funds are transferred instantly to your bank account, ensuring speed and reliability.</p>
          </div>
        </div>
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
      document.querySelectorAll('.fade-in, .stagger').forEach(el => observer.observe(el));
      </script>
    </body>
    </html>
    """
    components.html(how_it_works, height=450, scrolling=False)