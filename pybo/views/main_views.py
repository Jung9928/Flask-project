from flask import Blueprint, url_for
from werkzeug.utils import redirect
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

# bp는 Blueprint 클래스로 생성한 객체를 의미.
# Blueprint 클래스로 객체를 생성 시, 이름, 모듈명, URL prefix값을 전달해야 함.
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    # Question.query.order_by로 질문 목록 얻기 (order_by 함수는 조회 결과 정렬)
    # question_list = Question.query.order_by(Question.create_date.desc())
    return redirect(url_for('question._list'))