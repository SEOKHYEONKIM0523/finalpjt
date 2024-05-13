import sqlalchemy
from sqlalchemy.orm import sessionmaker
from settings import config

# from api.models.member import Base
from api.models.member import Base


engine = sqlalchemy.create_engine(config.db_conn, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(engine)


# 데이터베이스 세션 의존성 생성
# def get_db():
#     db = sess.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# 새버전
def get_db():
    with SessionLocal() as db:
        yield db
