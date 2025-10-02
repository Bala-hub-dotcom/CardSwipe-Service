import subprocess
import os
import time

# Start Streamlit server if not already running
if not os.path.exists("/tmp/streamlit_started"):
    with open("/tmp/streamlit_started", "w") as f:
        f.write("1")
    subprocess.Popen(
        ["streamlit", "run", "streamlit_app.py", "--server.port", "8501", "--server.headless", "true"]
    )
    time.sleep(5)  # give it some time to boot up

def handler(request, response):
    # Redirect to streamlit server
    response.status_code = 302
    response.headers["Location"] = "http://localhost:8501"
    return response
