from flask import Flask, request, jsonify
import re
from werkzeug.security import generate_password_hash  # For hashing the password

app = Flask(__name__)

# Regular expression to check for strong passwords
PASSWORD_REGEX = re.compile(
    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
)

def is_strong_password(password):
    # Check if the password matches the regular expression
    return PASSWORD_REGEX.match(password) is not None

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()  # Safely parse JSON from the request body

    # Validate that data contains 'username' and 'password'
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required.'}), 400

    username = data.get('username').strip()  # Strip spaces from username
    password = data.get('password')

    # Validate username and password
    if not username:  # Ensure username is not empty or just whitespace
        return jsonify({'error': 'Username cannot be empty.'}), 400

    if not is_strong_password(password):
        return jsonify({
            'error': 'Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a digit, and a special character.'
        }), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Here you would add logic to save the new user to your database
    # For example:
    # user = User(username=username, password=hashed_password)
    # db.session.add(user)
    # db.session.commit()

    return jsonify({'message': 'User signed up successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)  # Change this to `debug=os.environ.get('FLASK_DEBUG')` in production
