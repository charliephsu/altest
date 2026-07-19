from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from typing import List
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    chat_list: Mapped[List["ChatModel"]] = relationship()

    def __repr__(self) -> str:
        return(f"<User(id={self.id}, name={self.name})")

class Character(Base):
    __tablename__ = "characters"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    persona: Mapped[str]

    def __repr__(self) -> str:
        return(f"<Character(id={self.id}, name={self.name})")
    
class ChatModel(Base):
    __tablename__ = "chats"
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="chat_list")
    character_id: Mapped[str] = mapped_column(ForeignKey("characters.id"))
    chat_thing: Mapped[str] 


    def __repr__(self) -> str:
        return(f"<ChatModel(id={self.id}, chat_thing={self.chat_thing})")
