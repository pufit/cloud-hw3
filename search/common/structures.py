import typing as tp

from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: int
    gender: str
    age: int


class BaseSearchRequest(BaseModel):
    search_text: str
    user_data: User = Field(
        default_factory=lambda: User(
            user_id=-1,
            gender='non-existing gender',
            age=-1
        )
    )

    limit: int = 10


class Document(BaseModel):
    document: str
    key: str
    key_md5: str
    gender: str
    age_from: int
    age_to: int
    region: str


class DocumentList(BaseModel):
    documents: tp.List[Document] = []


class OutputDocument(BaseModel):
    document: str
    key: str
    key_md5: str


class SearchResult(BaseModel):
    documents: tp.List[OutputDocument] = []
