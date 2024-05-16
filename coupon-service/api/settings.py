# from pydantic_settings  import BaseSettings
# import os
# from dotenv import load_dotenv

# load_dotenv()

# SECRET_ENV = os.getenv("SECRET_ENV")

# class Settings(BaseSettings):
#     userid: str = SECRET_ENV
#     passwd: str = SECRET_ENV
#     dbname: str = SECRET_ENV
#     host: str = '13.124.149.113'  # MariaDB 호스트 주소
#     port: int = 3306  # MariaDB 포트
#     charset: str = 'utf8mb3'

#     # 데이터베이스 연결 문자열 정의
#     db_conn: str = f'mysql+pymysql://{userid}:{passwd}@{host}:{port}/{dbname}?charset={charset}'

# config = Settings()
