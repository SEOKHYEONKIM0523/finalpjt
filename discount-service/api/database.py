import sqlalchemy

from sqlalchemy.orm import sessionmaker
from settings import config


engine = sqlalchemy.create_engine(config.db_conn, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# 서버시작시 테이블 생성
def db_startup():
    from api.models import discount
    discount.Base.metadata.create_all(engine)