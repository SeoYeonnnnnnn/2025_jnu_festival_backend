from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. 데이터베이스 연결 설정
DATABASE_URL = "sqlite:///./2025_jnu_festival.db"

# 2. SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} # SQLite는 이 설정이 필요합니다.
)

# 3. 데이터베이스 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. 모델 클래스가 상속할 Base 클래스 생성
Base = declarative_base()

# 5. DB 세션을 가져오는 함수 (API 요청마다 독립적인 세션 생성)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
