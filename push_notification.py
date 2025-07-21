import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Load notification data from JSON
with open('data.json', 'r') as f:
    data = json.load(f)

title = data.get("title", "Notification")
body = data.get("body", "You have a new alert.")
icon = data.get("icon", "")

# Configure Chrome options
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")  # Optional: allow notifications
options.add_argument("--start-maximized")

# Start browser
driver = webdriver.Chrome(options=options)

# Load a blank page
driver.get("data:text/html,<html><head><title>Push Bot</title></head><body></body></html>")

# Wait to ensure browser is ready
time.sleep(1)

# Inject JS to trigger Notification API
js_code = f"""
if (Notification.permission !== 'granted') {{
    Notification.requestPermission().then(function(permission) {{
        if (permission === 'granted') {{
            new Notification("{title}", {{
                body: "{body}",
                icon: "{icon}"
            }});
        }}
    }});
}} else {{
    new Notification("{title}", {{
        body: "{body}",
        icon: "{icon}"
    }});
}}
"""

driver.execute_script(js_code)

# Wait before closing so user can see it
time.sleep(5)
driver.quit()