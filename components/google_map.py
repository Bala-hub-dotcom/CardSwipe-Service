import streamlit.components.v1 as components

def render_google_map():
    """Render a Google Map embed (adjust query if you want a specific address)."""
    html = """
    <style>
      .map-wrap { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }
      .map-iframe { width: 100%; height: 380px; border: 0; border-radius: 12px; box-shadow: 0 10px 24px rgba(0,0,0,.25); }
      @media (max-width: 560px) { .map-iframe { height: 300px; } }
    </style>
    <section>
      <div class="map-wrap">
        <iframe class="map-iframe" src="https://www.google.com/maps?q=Hyderabad&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </section>
    """
    components.html(html, height=420, scrolling=False)
