from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chart/')
def chart():
    return render_template('chart.html')