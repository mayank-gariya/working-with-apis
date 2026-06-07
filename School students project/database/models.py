from pydantic import BaseModel
from datetime import datetime

class School(BaseModel):
    name:str = 'nonu500'
    class_studed : str
    age : int 
    contact : int = 90909090
    marks : int
    tags : str = 'sudhra hai'
    leaved : bool = False
    