from app.models.user import UserReg, UserLog
from sqlalchemy.orm import Session
from app.database.models import User
import hashlib
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT


def ResponseRegister(user: UserReg, db: Session, Authorize: AuthJWT):
    password_hash = hashlib.sha256(user.password.encode()).hexdigest()
    email_check = db.query(User).filter(User.email == user.email).first()
    if email_check:
        return JSONResponse(content={"message": "user already exists"},
                            status_code=400)
    new_user = User(first_name=user.first_name, last_name=user.last_name,
                    email=user.email, password_hash=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = Authorize.create_access_token(subject=new_user.id)
    refresh_token = Authorize.create_refresh_token(subject=new_user.id)
    return JSONResponse(content={"access_token": access_token,
                                 "refresh_token": refresh_token},
                        status_code=200)


def ResponseLogin(user: UserLog, db: Session, Authorize: AuthJWT):
    email_check = db.query(User).filter(User.email == user.email).first()
    if email_check is None:
        return JSONResponse(content={"message": "incorrect email"},
                            status_code=403)
    password_hash = hashlib.sha256(user.password.encode()).hexdigest()
    if password_hash != email_check.password_hash:
        return JSONResponse(content={"message": "incorrect password"},
                            status_code=403)
    access_token = Authorize.create_access_token(subject=email_check.id)
    refresh_token = Authorize.create_refresh_token(subject=email_check.id)
    return JSONResponse(content={"access_token": access_token,
                                 "refresh_token": refresh_token},
                        status_code=200)
