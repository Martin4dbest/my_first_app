
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'd5ddffb27ee8f32e596e1d618eeb4bb4'
db = SQLAlchemy(app)

# Define your User model (replace this with your actual User model)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

# Initialize Flask-Admin
admin = Admin(app, name='My App Admin', template_mode='bootstrap3')

# Add your User model to Flask-Admin
admin.add_view(ModelView(User, db.session))

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
