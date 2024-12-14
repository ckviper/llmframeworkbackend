from pydantic import BaseModel, EmailStr, validator
import re


class UserReg(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    @validator("password")
    def validate_password(cls, value):
        # Проверка на минимальную длину
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        # Проверка на наличие цифры
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")
        # Проверка на наличие спецсимвола
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least \
                             one special character")
        return value


class UserLog(BaseModel):
    email: str
    password: str
