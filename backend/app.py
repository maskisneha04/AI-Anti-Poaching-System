from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/status")
def status():
    return jsonify({
        "system": "AI Anti-Poaching Wildlife Monitoring System",
        "status": "Active",
        "detection": "No Threat Detected"
    })

if __name__ == "__main__":
    app.run(debug=True)
