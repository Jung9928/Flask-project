# pybo.db라는 db파일을 프로젝트의 루트 디렉토리인 myproject에
# 저장하는 작업

import os

BASE_DIR = os.path.dirname(__file__)
# DB 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLAlchemy의 이벤트를 처리하는 옵션 (False로 비활성화)
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 실제 서비스 운영할 때는 유추하기 어려운 문자열로 바꿔주는게 보안상 좋다.
SECRET_KEY = "dev"