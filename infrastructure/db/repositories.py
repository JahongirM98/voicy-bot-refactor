from infrastructure.db.models import users

class UserRepository:
    def __init__(self, session):
        self.session = session

    def get_by_social_id(self, social_id: int):
        stmt = users.select().where(users.c.social_id == social_id)
        result = self.session.execute(stmt).fetchone()
        return result

    def get_by_id(self, user_id: int):
        stmt = users.select().where(users.c.id == user_id)
        result = self.session.execute(stmt).fetchone()
        return result

    def create(self, social_id: int, username: str, registration_date=None, taps=0, name=None, info=None, photo=None):
        stmt = users.insert().values(
            social_id=social_id,
            username=username,
            registration_date=registration_date,
            taps=taps,
            name=name,
            info=info,
            photo=photo
        )
        self.session.execute(stmt)

    def update(self, user_id: int, **kwargs):
        stmt = users.update().where(users.c.id == user_id).values(**kwargs)
        self.session.execute(stmt)

    def delete(self, user_id: int):
        stmt = users.delete().where(users.c.id == user_id)
        self.session.execute(stmt)

    def list_top_users(self, limit: int = 10):
        stmt = users.select().order_by(users.c.taps.desc()).limit(limit)
        result = self.session.execute(stmt).fetchall()
        return result