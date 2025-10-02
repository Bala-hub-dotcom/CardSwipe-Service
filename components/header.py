import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def render_header():
    if "header_rendered" not in st.session_state:
        logo_base64 = get_base64_image("./assets/Sri Gayatri traders.png")

        st.markdown(
            f"""
<style>
html {{
  scroll-behavior: smooth;
}}

.navbar {{
  position: sticky;
  top: 0;
  z-index: 1000;
  margin: 0;
  margin-top: 2rem;
  padding: 0;
  width: 100%;
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 12px 28px rgba(0,0,0,0.25);
  font-family: 'Segoe UI', sans-serif;
}}

.navbar-inner {{
  max-width: 1200px;
  margin: 0 auto;
  padding: .9rem 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}}

.brand {{
  display: flex;
  align-items: center;
  gap: .6rem;
  font-weight: 900;
  font-size: 1.2rem;
  color: #facc15;
}}

.brand img {{
  height: 36px;
  border-radius: 6px;
}}

.nav-links {{
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
}}

.nav-link {{
  color: white !important;
  text-decoration: none !important;
  padding: 0.65rem 1rem;
  border-radius: 8px;
  transition: all .2s ease;
  font-size: 0.95rem;
}}

.nav-link:hover {{
  background: rgba(255,255,255,.08);
  transform: translateY(-1px);
}}

.nav-link.active {{
  background: rgba(96,165,250,.18);
  border: 1px solid rgba(96,165,250,.35);
}}

.nav-link.whatsapp {{
  background-color: #facc15;
  color: white !important;
  box-shadow: 0 4px 10px rgba(250, 204, 21, 0.35);
}}

.nav-link.whatsapp:hover {{
  background-color: #fbbf24;
  box-shadow: 0 4px 10px rgba(250, 191, 36, 0.45);
}}

.menu-toggle {{
  display: none;
  font-size: 1.4rem;
  color: white;
  background: none;
  border: none;
  cursor: pointer;
}}

@media (max-width: 820px) {{
  .menu-toggle {{
    display: block;
  }}
  .nav-links {{
    flex-direction: column;
    overflow: hidden;
    max-height: 0;
    transition: max-height 0.4s ease;
    width: 100%;
    margin-top: .2rem;
  }}
  .nav-links.open {{
    max-height: 500px;
  }}
}}


</style>

<nav class="navbar" role="navigation" aria-label="Main Navigation">
  <div class="navbar-inner">
    <div class="brand">
      <img src="data:image/png;base64,{logo_base64}" alt="Logo" />
      <span>Sri Gayathri Traders</span>
    </div>
    <button class="menu-toggle" onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    <div id="nav-links" class="nav-links">
      <a class="nav-link" href="#home">Home</a>
      <a class="nav-link" href="#how-it-works">How It Works</a>
      <a class="nav-link" href="#services">Services</a>
      <a class="nav-link" href="#why-us">Why Us</a>
      <a class="nav-link" href="#reviews">Reviews</a>
      <a class="nav-link" href="#faq">FAQ</a>
      <a class="nav-link" href="#contact">Contact</a>
      <a class="nav-link whatsapp" href="https://wa.me/919505870597" target="_blank">WhatsApp Us</a>
    </div>
  </div>
</nav>
""",
            unsafe_allow_html=True,
        )

        st.markdown("""
<script>
document.addEventListener("DOMContentLoaded", function() {
  const toggle = document.querySelector(".menu-toggle");
  const navLinks = document.getElementById("nav-links");
  toggle.addEventListener("click", function() {
    navLinks.classList.toggle("open");
  });
  navLinks.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("open");
    });
  });
});
</script>
""", unsafe_allow_html=True)

        st.session_state.header_rendered = True