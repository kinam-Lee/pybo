from flask import Blueprint, render_template, url_for
from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Nice to meet U~'

@bp.route('/')
def index():
    #question_list = Question.query.order_by(Question.create_date.desc())
    #return render_template('question/question_list.html', question_list=question_list)
    #return 'This is Index Page~'

    return redirect(url_for('question._list'))

