# scrape_ibegin_playwright.py
from playwright.sync_api import sync_playwright
import time

URL = "https://careers.tietoevry.com/job/sr-rpa-developer-ui-path-tietoevry-create-m-f-d-in-bengaluru-india-jid-789?_atxsrc=AttraxLinkedin&utm_source=AttraxLinkedin"

def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)   # set headless=False to watch
        page = browser.new_page()
        page.goto(URL, timeout=60000)
        # Wait for network + rendering. Increase if your connection is slow.
        page.wait_for_load_state("networkidle", timeout=15000)
        time.sleep(2)

        # Save screenshot and HTML to inspect locally
        page.screenshot(path="ibegin_rendered.png", full_page=True)
        html = page.content()
        with open("ibegin_rendered.html", "w", encoding="utf-8") as f:
            f.write(html)

        # Example heuristics to extract data: adjust selectors after inspecting saved HTML
        def maybe_text(selector):
            try:
                el = page.query_selector(selector)
                return el.inner_text().strip() if el else None
            except:
                return None

        job_title = maybe_text("h1") or maybe_text(".job-title") or maybe_text("[data-test='jobTitle']")
        apply_by = maybe_text(".apply-by") or maybe_text("[data-test='dateApplyBy']")
        location = maybe_text(".location") or maybe_text("[data-test='location']")
        description = maybe_text(".job-description") or maybe_text(".description") or None

        print("job_title:", job_title)
        print("apply_by:", apply_by)
        print("location:", location)
        print("description (first 200 chars):", (description or "")[:200])

        browser.close()

if __name__ == "__main__":
    run()
