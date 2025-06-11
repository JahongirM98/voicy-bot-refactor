from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from infrastructure.db.repositories import UserRepository

# Используй такую же строку подключения, как в docker-compose и alembic.ini
DATABASE_URL = "postgresql://postgres:postgres@db:5432/voicy"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class UnitOfWork:
    def __enter__(self):
        self.session = Session()
        self.users = UserRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()