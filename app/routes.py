from flask import Blueprint, render_template
import os

templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
main_blueprint = Blueprint('main', __name__, template_folder=templates_dir)

@main_blueprint.route('/')
def home():
    return render_template('index.html')
