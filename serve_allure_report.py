import os
import http.server
import socketserver

# Directory where allure-results are stored
RESULTS_DIR = "allure-results"
REPORT_DIR = "allure-report"

# Add the virtual environment's Scripts directory to PATH using a relative path
VENV_PATH = os.path.join(os.getcwd(), ".venv", "Scripts")
os.environ["PATH"] = f"{VENV_PATH};" + os.environ["PATH"]

# Generate the report
os.system(f"allure generate {RESULTS_DIR} -o {REPORT_DIR} --clean")

# Serve the report
PORT = 8000
os.chdir(REPORT_DIR)
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving Allure report at http://localhost:{PORT}")
    httpd.serve_forever()