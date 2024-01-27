from flask import Blueprint, render_template
import time

set = Blueprint('settings', __name__, url_prefix='/settings')

@set.route('/', methods=['GET'])
def dashboard():
	time.sleep(3)
	return render_template('set/settings.html')