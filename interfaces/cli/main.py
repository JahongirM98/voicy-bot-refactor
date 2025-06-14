import typer
from services.user_service import UserService
from infrastructure.db.uow import UnitOfWork

cli = typer.Typer()
user_service = UserService(UnitOfWork)

@cli.command()
def register(social_id: int, username: str):
    user = user_service.register_user(social_id, username)
    if user:
        typer.echo(f"User {user.username} зарегистрирован!")
    else:
        typer.echo("Ошибка регистрации.")

@cli.command()
def top(limit: int = 10):
    top_users = user_service.get_top_users(limit)
    for user in top_users:
        typer.echo(f"{user.username} — taps: {user.taps}")

@cli.command()
def list_users():
    users = user_service.get_top_users(100)
    for user in users:
        typer.echo(f"{user.username} (id: {user.id}, taps: {user.taps})")

@cli.command()
def update_user(social_id: int, name: str = None, info: str = None):
    result = user_service.update_profile(social_id, name=name, info=info)
    typer.echo("Профиль обновлён" if result else "Пользователь не найден.")

@cli.command()
def delete_user(social_id: int):
    with UnitOfWork() as uow:
        user = uow.users.get_by_social_id(social_id)
        if user:
            uow.users.delete(user.id)
            typer.echo("Пользователь удалён")
        else:
            typer.echo("Пользователь не найден")


if __name__ == "__main__":
    cli()
