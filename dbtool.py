from DBModel import Base,User,Character,ChatModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import select


import sys


engine = create_engine("sqlite+pysqlite:///database.sqlite", echo=True)


def create_table():
    print(f"creating tables")
    Base.metadata.create_all(engine)
   
def add_users():
    print(f"Adding users")
    user_id_001 = "100"
    user_001 = User(id=user_id_001, name="Joe Test", age=20)

    user_id_002 = "101"
    user_002 = User(id=user_id_002, name="Roger Foo", age=25)

    with Session(engine) as session:
        session.add_all([user_001,user_002])
        session.commit()


def add_characters():
    print(f"Adding Characters")
    character_id_001 = "200"
    character_1 = Character(id=character_id_001, name="Fantasy School", persona="A magical school")

    character_id_002 = "201"
    character_2 = Character(id=character_id_002, name="Modern High School", persona="High school in America")
    with Session(engine) as session:
        session.add_all([character_1,character_2])
        session.commit()


def add_chats():
    print(f"Adding Chats")
    chat_id_001 = "400"
    chat_1 = ChatModel(id=chat_id_001, user="100", character="200", chat_thing="thing one")

    chat_id_001 = "401"
    chat_2 = ChatModel(id=chat_id_001, user="100", character="200", chat_thing="thing two")


    with Session(engine) as session:
        session.add_all([chat_1,chat_2])
        session.commit()



def get_users():
    print(f"Users")
    Session = sessionmaker(engine)

    with Session.begin() as session:
        stmt = select(User)
        results = session.scalars(stmt).all()
        session.expunge_all()

    print("-----------------")
    for item in results:
        print(f"Id: {item.id}, Name: {item.name}, Age: {item.age} ")
 
def get_characters():
    print(f"Characters")
    Session = sessionmaker(engine)

    with Session.begin() as session:
        stmt = select(Character)
        results = session.scalars(stmt).all()
        session.expunge_all()

    print("-----------------")
    for item in results:
        print(f"Id: {item.id}, Name: {item.name}, Persona: {item.persona} ")

def get_chats():
    print(f"Chats")
    Session = sessionmaker(engine)

    with Session.begin() as session:
        stmt = select(ChatModel)
        results = session.scalars(stmt).all()
        session.expunge_all()

    print("-----------------")
    for item in results:
        print(f"Id: {item.id}, chat_thing: {item.chat_thing}")




def drop_tables():
    print(f"dropping tables")
    Base.metadata.drop_all(engine)


def addall():
    add_users()
    add_characters()
    add_chats()

def dropadd():
    drop_tables()
    create_table()
    addall()

def help(help_string = ""):
    if help_string:
        print(f"{help_string}")
    print(f"dbtool: create | drop | add_users | get_users | add_characters | get_characters | add_chats | get_chats | addall | dropadd")

if __name__ == '__main__':     
    if len(sys.argv) < 2:
        com = ""
    else:
        com = sys.argv[1]

    print("Database tool")
    print("========================================")

    match com:
        case "create":
            create_table()
        case "drop":
            drop_tables()
        case "add_users":
            add_users()
        case "add_characters":
            add_characters()
        case "get_users":
            get_users()
        case "get_characters":
            get_characters()
        case "add_chats":
            add_chats()
        case "get_chats":
            get_chats()
        case "addall":
            addall()
        case "dropadd":
            dropadd()

        case _:
            help()

