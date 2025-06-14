from infrastructure.db.uow import UnitOfWork

class UserService:
    def __init__(self, uow_factory):
        self.uow_factory = uow_factory

    def register_user(self, social_id: int, username: str):
        with self.uow_factory() as uow:
            user = uow.users.get_by_social_id(social_id)
            if user:
                return user
            uow.users.create(social_id=social_id, username=username)
            return uow.users.get_by_social_id(social_id)

    def update_profile(self, social_id: int, **fields):
        with self.uow_factory() as uow:
            user = uow.users.get_by_social_id(social_id)
            if user:
                uow.users.update(user.id, **fields)
                return True
            return False

    def get_user(self, social_id: int):
        with self.uow_factory() as uow:
            return uow.users.get_by_social_id(social_id)

    def get_top_users(self, limit: int = 10):
        with self.uow_factory() as uow:
            return uow.users.list_top_users(limit)
