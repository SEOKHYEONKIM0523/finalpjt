import uvicorn
from api.routes import coupon
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

import database as sess

app = FastAPI()
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

templates = Jinja2Templates(directory='/views/templates')

# CORS 설정
origins = [
    "http://54.180.228.64:32321",  # 허용할 프론트엔드 도메인
    "http://54.180.228.64:30742",
    "http://54.180.228.64:32323",
    "http://54.180.228.64:32322",
    "http://54.180.228.64:32324"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(coupon.router)

if __name__ == '__main__':
    sess.create_tables()
    uvicorn.run('main:app', host="0.0.0.0", port=8040, reload=True)
