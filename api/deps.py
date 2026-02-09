
from typing import Any, AsyncGenerator

from fastapi import Depends,  HTTPException, Request

from api.services.admin_service import AdminService
from api.services.user_service import UserService
from database.db import db
from database.repository.admin_repository import AdminRepository
from database.repository.clients_repository import ClientRepository
from database.repository.payments_repository import PaymentRepository
from database.repository.subscription_repository import SubscriptionRepository


# ---------- DB ----------
async def get_session() -> AsyncGenerator[Any, Any]:
    async with db.session() as session:
        yield session

# ---------- SERVICES ----------
def get_admin_service(
        session=Depends(get_session),
) -> AdminService:
    return AdminService(
        client_repo=ClientRepository(session),
        sub_repo=SubscriptionRepository(session),
        admin_repo=AdminRepository(session)
    )

def get_user_service(
        session=Depends(get_session),
) -> UserService:
    return UserService(
        client_repo = ClientRepository(session),
    sub_repo =SubscriptionRepository(session),
    payments_repo = PaymentRepository(session),
    )




