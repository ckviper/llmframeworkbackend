from pydantic import BaseModel, EmailStr, validator, Field
import re


class UserReg(BaseModel):
    first_name: str = Field(description="Имя юзера")
    last_name: str = Field(description="Фамилия юзера",)
    email: EmailStr = Field(description="Электорнная почта юзера")
    password: str = Field(description="Пароль юзера")

    @validator("first_name", "last_name")
    def validate_names(cls, value):
        # Проверка на минимальную длину
        if len(value) < 1:
            raise ValueError("names must be at least 1 characters long")
        # Проверка на наличие цифры
        if re.search(r"\d", value):
            raise ValueError("names musnt't contain number's")
        # Проверка на наличие спецсимвола
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("names musnt't contain special characters")
        return value

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
            raise ValueError("Password must contain at least one special character")
        return value


class UserLog(BaseModel):
    email: str = Field(description="Электорнная почта юзера")
    password: str = Field(description="Пароль юзера")
