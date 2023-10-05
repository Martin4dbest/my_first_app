from flask import Flask
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize the database
db.init_app(app)

@app.route('/')
def index():
    # Your code here
    return 'Hello, World!'

@app.route('/create_user')
def create_user():
    user = User(name='John Doe', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    return 'User created successfully!'

@app.route('/get_users')
def get_users():
    users = User.query.all()
    return f"All users: {users}"

@app.route('/update_email')
def update_email():
    user = User.query.filter_by(name='John Doe').first()
    if user:
        user.email = 'newemail@example.com'
        db.session.commit()
        return 'Email updated successfully!'
    else:
        return 'User not found!'

@app.route('/delete_user')
def delete_user():
    user = User.query.filter_by(name='John Doe').first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully!'
    else:
        return 'User not found!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
