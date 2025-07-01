from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from ..core.config import get_settings


# To be expanded: This is a stub for database connection.


# PUBLIC_INTERFACE
def get_db():
    """
    Yields a database session.
    """
    settings = get_settings()
    # In future, pool_pre_ping and engine config can be improved
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
