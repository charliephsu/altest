
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine
from DBModel import Base,User,Character,ChatModel
from sqlalchemy.orm import joinedload


engine = create_engine("sqlite+pysqlite:///database.sqlite", echo=True)


def get_users():
    print(f"Users")
    Session = sessionmaker(engine)


    with Session.begin() as session:
        stmt = select(User).options(joinedload(User.chat_list))
        results = session.execute(stmt).unique().scalars().all()
        session.expunge_all()


    print("-----------------")
    for item in results:
        print(f"Id: {item.id}, Name: {item.name}, Age: {item.age}, list: {item.chat_list} ")

    return results

def get_chats():
    print("Chats")
    Session = sessionmaker(engine)


    with Session.begin() as session:
        stmt = select(ChatModel)
        results = session.execute(stmt).scalars().all()

        res = []
        for item in results:
            #print(item)
            #print(f"{item.user}")
            new_chat = {
                "id": item.id,
                "chat_thing": item.chat_thing,
                "user_name": item.user.name
            }
            res.append(new_chat)

        session.expunge_all()


    print("----------")
    for row in res:
        print(row)


def get_chat2():
    print("Chats")
    Session = sessionmaker(engine)

    # this is how to do eager loading
    with Session.begin() as session:
        stmt = select(ChatModel).options(joinedload(ChatModel.user))
        results = session.execute(stmt).unique().scalars().all()
        session.expunge_all()


    for item in results:
        print(item)
        print(item.user)

def test():
    pass


def main():
    print("Hello from altest!")

    get_chat2();


if __name__ == "__main__":
    main()
