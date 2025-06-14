from infrastructure.db.uow import UnitOfWork

class TapsService:
    def __init__(self, uow_factory):
        self.uow_factory = uow_factory

    def increment_taps(self, social_id: int):
        with self.uow_factory() as uow:
            user = uow.users.get_by_social_id(social_id)
            if user:
                new_taps = (user.taps or 0) + 1
                uow.users.update(user.id, taps=new_taps)
                return new_taps
            return None

    def reset_taps(self, social_id: int):
        with self.uow_factory() as uow:
            user = uow.users.get_by_social_id(social_id)
            if user:
                uow.users.update(user.id, taps=0)
                return True
            return False