from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event 


class User(BaseModel): 
    email: str 
    password: str 
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packtl.com",
                "username": "strong"
            }
        }
    
class NewUser(User):
    pass
    

class UserSignIn(BaseModel): 
    email: str
    password: str 
    
    class Config: 
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com", 
                "password": "strong"
            }
        }
