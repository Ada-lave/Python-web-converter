from pydantic import BaseModel

class BaseFile(BaseModel):
    name:str
    file_type_id: int
    size: int