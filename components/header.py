import streamlit as st

def render_header():
    st.markdown(
        """
<style>
/* Full navbar styling */
.navbar {
  position: sticky; top: 0; z-index: 1000;
  margin-top: 10px; /* add space above header */
  width: 100%;
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 12px 28px rgba(0,0,0,0.25);
}
.navbar-inner { max-width: 1200px; margin: 0 auto; padding: .9rem 1rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.brand { font-weight: 900; letter-spacing: -0.02em; text-decoration: none; color: #e2e8f0; display: inline-flex; align-items: center; gap: .6rem; }
.brand .grad { background: linear-gradient(90deg, #60a5fa, #22c55e); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.nav-links { display: flex; align-items: center; gap: .5rem; }
.nav-link { color: #e2e8f0; text-decoration: none; padding: .45rem .75rem; border-radius: 10px; transition: all .2s ease; opacity: .95; }
.nav-link:hover { background: rgba(255,255,255,.08); transform: translateY(-1px); }
.nav-link.active { background: rgba(96,165,250,.18); border: 1px solid rgba(96,165,250,.35); }
.nav-link.whatsapp { background: linear-gradient(135deg, #25D366, #128C7E); color: #fff; box-shadow: 0 10px 25px rgba(37,211,102,.35); }
.nav-link.whatsapp:hover { box-shadow: 0 14px 35px rgba(37,211,102,.45); }
.menu-toggle { display: none; color: #e2e8f0; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.2); padding: .35rem .6rem; border-radius: 8px; }
@media (max-width: 820px) { .menu-toggle { display: inline-flex; } .nav-links { display: none; } .nav-links.open { display: grid; grid-template-columns: repeat(3, 1fr); gap: .5rem; margin-top: .5rem; } .navbar-inner { flex-wrap: wrap; } }
</style>

<nav id=\"top-navbar\" class=\"navbar\">
  <div class=\"navbar-inner\">
    <a href=\"#home\" class=\"brand\"><span class=\"grad\">💳 Sri Gayathri Traders</span></a>
    <button id=\"menu-toggle\" class=\"menu-toggle\" aria-label=\"Toggle menu\">☰</button>
    <div id=\"nav-links\" class=\"nav-links\">
      <a class=\"nav-link\" href=\"#home\">Home</a>
      <a class=\"nav-link\" href=\"#how-it-works\">How It Works</a>
      <a class=\"nav-link\" href=\"#services\">Services</a>
      <a class=\"nav-link\" href=\"#why-us\">Why Us</a>
      <a class=\"nav-link\" href=\"#reviews\">Reviews</a>
      <a class=\"nav-link\" href=\"#faq\">FAQ</a>
      <a class=\"nav-link\" href=\"#contact\">Contact</a>
      <a class=\"nav-link whatsapp\" href=\"https://wa.me/919505870597\" target=\"_blank\">WhatsApp Us</a>
    </div>
  </div>
</nav>
<script>
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#menu-toggle');
    if (!btn) return;
    const links = document.getElementById('nav-links');
    if (links) links.classList.toggle('open');
  });
</script>
""",
        unsafe_allow_html=True,
    )
