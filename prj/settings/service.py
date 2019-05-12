from .common import *

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'prj_db',                  # DB 이름
        'USER':     'root',                    # DB 사용자 이름
        'PASSWORD': 'mysql1229',              # DB 비밀번호
        'HOST':     '127.0.0.1',               # DB 서버 주소
        'PORT':     '',                        # DB 포트 (생략하면 MySQL 디폴트 포트 3306 자동 지정)
        'OPTIONS':  {'charset': 'utf8mb4'},
    }
}