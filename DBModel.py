from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

class Character(Base):
    __tablename__ = "characters"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    persona: Mapped[str]

class ChatModel(Base):
    __tablename__ = "chats"
    id: Mapped[str] = mapped_column(primary_key=True)
    user: Mapped[str]
    character: Mapped[str]
    chat_thing: Mapped[str]
