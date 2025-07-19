from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from . import models
from .routers import booths

# 1. 데이터베이스 테이블 생성
# (만약 테이블이 이미 존재한다면, 이 코드는 아무것도 하지 않습니다)
models.Base.metadata.create_all(bind=engine)

# 2. FastAPI 앱 인스턴스 생성
app = FastAPI()

# 3. CORS 미들웨어 설정
# 프론트엔드(React)가 실행되는 주소(http://localhost:5173)에서의 요청을 허용합니다.
origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://127.0.0.1:5173",
    "http://172.16.6.58:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # 모든 HTTP 메소드 허용
    allow_headers=["*"], # 모든 HTTP 헤더 허용
)

# 4. 라우터 연결
# '/api/booths' 경로로 들어오는 요청은 booths.router가 처리하도록 설정합니다.
app.include_router(booths.router, prefix="/api/booths", tags=["booths"])


# 기본 경로 (서버가 살아있는지 확인하는 용도)
@app.get("/")
def read_root():
    return {"message": "Festival API is running!"}