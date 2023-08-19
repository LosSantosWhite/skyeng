from fastapi import APIRouter, status

from .schemas import UserRetrieve


user_login_router = APIRouter(prefix="/user", tags=["User registration & authorisation"])


@user_login_router.get("/login", status_code=status.HTTP_200_OK, response_model=UserRetrieve)