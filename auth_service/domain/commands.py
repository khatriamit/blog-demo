from pydantic import BaseModel as Model, validator


class RegisterUser(Model):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    # confirm_password: str

    # @validator("confirm_password")
    # def passwords_match(cls, v, values, **kwargs):
    #     print(v)
    #     if "password" in values and v != values["password"]:
    #         raise ValueError("passwords do not match")
    #     if len(v) < 8:
    #         raise ValueError("password must be minimum eight characters")
    #     if v.isalnum():
    #         raise ValueError("password must contain special characters")
    #     return v
