from infrastructure.db.uow import UnitOfWork

class TopService:
    def __init__(self, uow_factory):
        self.uow_factory = uow_factory

    def get_top_users(self, limit: int = 10):
        with self.uow_factory() as uow:
            return uow.users.list_top_users(limit)