
#imports the necessary libraries for the app to run the backend through your local machine/terminal

from flask import Flask, jsonify, session, redirect, url_for, request, abort
from msal import ConfidentialClientApplication
from data import employees  # Import sample data from data.py


#initialises a Flask application and sets a secret key for session management.
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Azure AD configuration
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
TENANT_ID = "your_tenant_id"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_PATH = "/auth/callback"
SCOPE = ["User.Read"]

#this handles authentication with Azure AD.

msal_app = ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
)

# Route for listing employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# Route for Azure AD login
@app.route("/login")
def login():
    auth_url = msal_app.get_authorization_request_url(SCOPE, redirect_uri=url_for("authorized", _external=True))
    return redirect(auth_url)

# Redirect endpoint after login
@app.route(REDIRECT_PATH)
def authorized():
    if request.args.get("code"):
        token_response = msal_app.acquire_token_by_authorization_code(
            request.args["code"], SCOPE, redirect_uri=url_for("authorized", _external=True)
        )
        session["user"] = token_response.get("id_token_claims")
    return redirect(url_for("home"))

# Role-based access control example
def role_required(role):
    def wrapper(f):
        def decorated_function(*args, **kwargs):
            if "user" not in session or session["user"].get("roles") != role:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route("/admin-dashboard")
@role_required("Admin")
def admin_dashboard():
    return "Welcome to the Admin Dashboard"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


