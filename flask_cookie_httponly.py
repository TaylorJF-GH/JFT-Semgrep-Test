# flask_cookie_httponly_bad.py
# WARNING: Intentionally insecure Flask example.
# Sets a cookie with HttpOnly disabled.
# For testing analyzers (Semgrep, Bandit, etc.) ONLY.

from flask import Flask, make_response

app = Flask(__name__)

@app.route("/set_insecure_cookie")
def set_insecure_cookie():
    resp = make_response("Insecure cookie has been set.")
    # BAD: HttpOnly is explicitly disabled
    resp.set_cookie("session_id", "12345", httponly=False, secure=False)
    return resp

if __name__ == "__main__":
    app.run(debug=True)
