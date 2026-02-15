from dotenv import load_dotenv
from sqlalchemy import create_engine , text , Column , Integer , String
from sqlalchemy.orm import declarative_base , sessionmaker
import os

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , autoincrement=True)
    name = Column(String(30) , nullable=False)
    email = Column(String(100) , unique = True)

    def __init__(self,name,email= None):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"<User(id = {self.id}, name = {self.name}, email = {self.email})>"

load_dotenv()
database_url = os.getenv("DATABASE_URL")
try:
    engine = create_engine(database_url)
    Session = sessionmaker(bind = engine)
    print("Database connection established")
except Exception as e:
    print(f"Database is not created {e}")
else:
    session = Session()
    Base.metadata.create_all(engine)
    new_user1 = User('Deep', 'deep@gmail.com')
    new_user2 = User('Yash')
    try:
        # session.add_all([new_user1,new_user2])

        all_users = session.query(User).all()
        print(f"All users:{all_users}")

        # user_by_id = session.query(User).get(2)
        # print(f"user with id:{user_by_id}")

        # user_startwith_A = session.query(User).filter(User.name.startswith('A')).all()
        # print(user_startwith_A)

        # user_update = session.query(User).filter_by(name = 'Ashish').first()
        # if user_update:
        #     print(user_update)
        #     user_update.email = 'Ashish'
        #     print(f"email of {user_update.name} updated successfully")
        # else:
        #     print("User Not Found")
            
        user_to_delete = session.query(User).filter_by(name = 'yash').first()
        print(user_to_delete)
        session.delete(user_to_delete)
        
        session.commit()
        session.close()
        # print("User added successfully")
    except Exception as e:
        print(f"Error..: {e}")
    else:
        session.close()