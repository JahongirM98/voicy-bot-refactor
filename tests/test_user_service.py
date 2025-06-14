from services.user_service import UserService
from infrastructure.db.uow import UnitOfWork

def test_register_user():
    service = UserService(UnitOfWork)
    user = service.register_user(123456, "pytest_user")
    assert user is not None
    assert user.username == "pytest_user"

def test_double_registration_returns_same_user():
    service = UserService(UnitOfWork)
    user1 = service.register_user(1234567, "pytest2")
    user2 = service.register_user(1234567, "pytest2")
    assert user1.id == user2.id
