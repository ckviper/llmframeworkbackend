from fastapi import APIRouter, Depends
from app.models.user import UserReg, UserLog
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.auth_service import ResponseRegister, ResponseLogin
from fastapi_jwt_auth import AuthJWT
from app.core.jwt.jwtset import jwt_required_decorator


router = APIRouter()


@router.post("/api/v1/register")
async def registration(user: UserReg,
                       db: Session = Depends(get_db),
                       Authorize: AuthJWT = Depends()):
    response = ResponseRegister(user, db, Authorize)
    return response


@router.post("/api/v1/login")
async def authorization(user: UserLog,
                        db: Session = Depends(get_db),
                        Authorize: AuthJWT = Depends()):
    response = ResponseLogin(user, db, Authorize)
    return response
