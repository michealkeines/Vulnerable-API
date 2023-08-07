from flask import render_template
from custom_db import setup_db 
import connexion

import os
try:
    os.remove("vulns.db")
except:
    pass

try:
    setup_db()
except:
    pass

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

