from pydantic import BaseModel


class DocumentBase(BaseModel):
    title: str
    contents: str


class DocumentCreate(DocumentBase):
    pass

class DocumentDelete(BaseModel):
    document_id: int
    user_token: str

class DocumentEdit(DocumentBase):
    document_id: int
    user_token: str

class Document(DocumentBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

class UserEdit(UserBase):
    password: str
    user_token: str

class UserDelete(BaseModel):
    user_token: str

class User(UserBase):
    id: int
    documents: list[Document] = []

    class Config:
        orm_mode = True

