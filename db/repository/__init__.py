from db.repository.admins_repo import AdminsRepository
from db.repository.ai_requests_repo import AiRequestsRepository
from db.repository.users_repo import UsersRepository

users_repository = UsersRepository()
admins_repository = AdminsRepository()
ai_requests_repository = AiRequestsRepository()

__all__ = ['users_repository', 'admins_repository', 'ai_requests_repository']


