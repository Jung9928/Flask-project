from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# create_app 함수는 애플리케이션 팩토리. (app 객체의 순환 참조를 방지)
def create_app():
    app = Flask(__name__)       # 플라스크 앱을 생성하는 코드 name이라는 변수에 모듈명이 담김.

    app.config.from_object(config)

    Markdown(app, extensions=['nl2br', 'fenced_code'])

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    # 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터.
    # @app.route와 같은 애너테이션으로 매핑되는 함수를 "라우트 함수"라고 한다.
    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app