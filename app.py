import requests
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)




auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin"),
    "admin2": generate_password_hash("admin2"),

}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required()
def hello_world():
    response = requests.get(url="https://carbonwatch.kayrros.com/power/europe")
    return (response.text).format(auth.current_user())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)