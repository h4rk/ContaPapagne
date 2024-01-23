from flask import Blueprint, render_template

set = Blueprint('settings', __name__, url_prefix='/settings')

@set.route('/', methods=['GET'])
def index():
	return render_template('settings.html')