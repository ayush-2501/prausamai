from flask import Blueprint, render_template
import os

# Set the template directory path
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')

# Initialize the Blueprint
main_blueprint = Blueprint('main', __name__, template_folder=templates_dir)

# Route for the home page
@main_blueprint.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@main_blueprint.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@main_blueprint.route('/contact')
def contact():
    return render_template('contact.html')
