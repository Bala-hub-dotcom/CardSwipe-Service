import streamlit as st

def resolve_image():
    """Resolve image path for the application"""
    try:
        # Try to load the local image
        return "assets/card image.png"
    except:
        # Fallback to placeholder if local image not found
        return "https://placehold.co/600x400/2563eb/white?text=Credit+Card+Service"