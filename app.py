import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sri Gayathri Traders - Credit Card Spot Cash",
    page_icon="💳",
    layout="wide",
)

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>
:root { --nav-h: 70px; --primary: #4F46E5; --light: #f9f9ff; }
html, body, [data-testid="stAppViewContainer"] { scroll-behavior: smooth; }

/* NAVBAR */
.topnav {
  position: sticky; top: 0; z-index: 1000;
  display: flex; justify-content: center; gap: 1rem;
  padding: 0.8rem; background: white;
  border-bottom: 1px solid #eee;
  box-shadow: 0 2px 2px rgba(0,0,0,0.05);
  margin-bottom: 1rem;
}
.topnav a {
  text-decoration: none; font-weight: 600;
  padding: 0.5rem 0.9rem;
  border-radius: 12px; transition: all 0.3s;
  color: #333;
}
.topnav a:hover { background: var(--light); color: var(--primary); }
.topnav a.active { background: var(--primary); color: white; }

/* SECTIONS + ANIMATIONS */
@keyframes fadeInUp { 0% {opacity:0; transform: translateY(40px);} 100% {opacity:1; transform: translateY(0);} }
@keyframes float { 0% {transform: translateY(0);} 50% {transform: translateY(-10px);} 100% {transform: translateY(0);} }

.section {
  padding: 2px; 
  min-height: auto;
  animation: fadeInUp 0.8s ease;
  background: white; 
  border-radius: 8px;
  margin: 10px 0; 
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
.anchor { 
  position: relative; 
  top: calc(-1 * var(--nav-h)); 
  visibility: hidden; 
  height: 0; 
}
.home-img img { 
  animation: float 3s ease-in-out infinite; 
  border-radius: 16px; 
  box-shadow: 0 6px 18px rgba(0,0,0,0.1);
  max-width: 100%;
}

/* FLOATING BUTTONS */
.floating-btn {
  position: fixed; 
  width: 60px; height: 60px; 
  right: 20px;
  border-radius: 50%; 
  text-align: center; 
  font-size: 30px;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
  z-index: 1000; 
  color: white; 
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: bounce 2s infinite, pulse 3s infinite;
  transition: transform 0.3s, box-shadow 0.3s;
}
.floating-btn:hover { transform: scale(1.2); box-shadow: 0 0 18px rgba(0,0,0,0.4); }
.whatsapp-float { bottom: 20px; background-color: #25d366; }
.call-float { bottom: 90px; background-color: #34b7f1; }

@keyframes bounce { 
  0%,20%,50%,80%,100% {transform: translateY(0);} 
  40% {transform: translateY(-6px);} 
  60% {transform: translateY(-3px);} 
}
@keyframes pulse { 
  0% {box-shadow: 0 0 0 0 rgba(0,0,0,0.3);} 
  70% {box-shadow: 0 0 0 15px rgba(0,0,0,0);} 
  100% {box-shadow: 0 0 0 0 rgba(0,0,0,0);} 
}

/* FOOTER */
.footer { 
  text-align: center; 
  padding: 20px; 
  margin-top: 20px; 
  font-size: 14px; 
  color: #666; 
  border-top: 1px solid #eee;
}
</style>
""", unsafe_allow_html=True)

# ---------- NAVBAR ----------
st.markdown("""
<div class="topnav" id="navbar">
  <a href="#home" class="active">Home</a>
  <a href="#how">How It Works</a>
  <a href="#services">Services</a>
  <a href="#why">Why Us</a>
  <a href="#reviews">Reviews</a>
  <a href="#faq">FAQ</a>
  <a href="#contact">Contact Us</a>
</div>
""", unsafe_allow_html=True)

# ---------- HOME ----------
st.markdown('<div id="home" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("💳 Instant Cash on Credit Cards – 24/7 Service")
        st.subheader("Sri Gayathri Traders | Hyderabad's Trusted Credit Card Swipe Service")
        st.write("We provide **secure, fast, and affordable** cash withdrawal on all major credit cards with just **2% service charge** and **zero utility charges**.")
        st.markdown("### 📱 Call or WhatsApp: **9505870597**")
        st.markdown("👉 Available 24/7 for emergency needs.")
    with col2:
        st.markdown('<div class="home-img">', unsafe_allow_html=True)
        # Using a placeholder image since the original path might not work
        st.image("https://placehold.co/600x400/4F46E5/FFFFFF?text=Sri+Gayathri+Traders",
                 caption="Spot Cash on All Credit Cards",
                 use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- HOW IT WORKS ----------
st.markdown('<div id="how" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("⚡ How It Works")
    st.markdown("""
    1. **Swipe Your Card** – Visit our center or connect via WhatsApp.  
    2. **Get Instant Cash** – Receive money on the spot or make payments directly.  
    3. **Secure & Transparent** – Flat **2% service charge**, no hidden costs.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SERVICES ----------
st.markdown('<div id="services" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("🛠️ Our Services")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("💵 Spot Cash")
        st.write("Withdraw cash instantly from any credit card with minimal charges.")
    with c2:
        st.subheader("🔄 Card-to-Card Transfer")
        st.write("Easily transfer balance between credit cards at just **2% fee**.")
    with c3:
        st.subheader("✈️ Travel & Bill Payments")
        st.write("Pay for flights, hotels, and utility bills hassle-free using your card.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- WHY US ----------
st.markdown('<div id="why" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("✅ Why Choose Us?")
    st.write("""
- **Lowest Fees in Hyderabad** – Flat **2% service charge**, no hidden costs.  
- **Instant Processing** – Get cash in hand within minutes.  
- **Secure & Confidential** – 100% trusted and verified transactions.  
- **All Banks Supported** – Visa, MasterCard, Rupay, AmEx, and more.  
- **24/7 Service** – We're available round the clock for your needs.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- REVIEWS ----------
st.markdown('<div id="reviews" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("⭐ Client Reviews")
    st.success("'Got cash in just 10 minutes. No extra charges. Best service in Hyderabad!' – Rajesh K.")
    st.info("'Helped me with urgent travel booking. Smooth and trustworthy.' – Priya S.")
    st.warning("'Professional, fast, and affordable. Highly recommended.' – Meena R.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FAQ ----------
st.markdown('<div id="faq" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("❓ Frequently Asked Questions")
    st.write("**Q: Is this service legal?** – ✅ Yes, we follow ID-verified legitimate processes.")
    st.write("**Q: Which cards do you accept?** – All major cards: Visa, MasterCard, AmEx, Rupay, Diner's Club.")
    st.write("**Q: How fast can I get cash?** – Within minutes, 24/7 availability.")
    st.write("**Q: Any hidden charges?** – None. Flat **2% service fee**, zero utility charges.")
    st.write("**Q: Do you provide loans?** – ❌ No. We only offer spot cash & swipe services.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- CONTACT ----------
st.markdown('<div id="contact" class="anchor"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📞 Contact Us")
    st.write("For quick service, reach out now:")
    st.markdown("### 📱 Call: [9505870597](tel:+919505870597)")
    st.markdown("### 💬 WhatsApp: [Click to Chat](https://wa.me/919505870597)")
    st.write("📍 Location: Hyderabd, Telangana")
    st.write("Available **24/7** for emergency needs.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FLOATING ACTION BUTTONS ----------
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<a href="https://wa.me/919505870597" class="floating-btn whatsapp-float" target="_blank">
  <i class="fab fa-whatsapp"></i>
</a>
<a href="tel:+919505870597" class="floating-btn call-float">
  <i class="fas fa-phone"></i>
</a>
""", unsafe_allow_html=True)

# ---------- AUTO-HIGHLIGHT NAVBAR ON SCROLL ----------
st.markdown("""
<script>
function updateNavHighlight() {
  const sections = document.querySelectorAll('.anchor');
  const navLinks = document.querySelectorAll('.topnav a');
  
  let currentSection = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (window.scrollY >= sectionTop - 100) {
      currentSection = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + currentSection) {
      link.classList.add('active');
    }
  });
}

// Initial call
updateNavHighlight();

// Listen for scroll events
window.addEventListener('scroll', updateNavHighlight);
</script>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
© 2025 Sri Gayathri Traders | All Rights Reserved.<br>
⚠️ Disclaimer: We do not provide personal loans. Our service is strictly card-based spot cash withdrawal.
</div>
""", unsafe_allow_html=True)