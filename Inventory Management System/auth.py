from database import UserModel
from sqlalchemy.orm import Session
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(session: Session):
    username = input("New Username: ")
    existing = session.query(UserModel).filter_by(username=username).first()
    if existing:
        print("\nUsername already exists")
        return
    password = input("Password: ")
    role = input("Role (Admin/Staff): ").lower()
    if role not in ["admin", "staff"]:
        print("\nInvalid role")
        return
    user = UserModel(username=username, password=hash_password(password),role=role)
    session.add(user)
    session.commit()
    print("\nRegistration successful")
    return user

def login(session: Session):
    username = input("Username: ")
    password = input("Password: ")
    user = session.query(UserModel).filter_by(username=username).first()
    if user and user.password == hash_password(password):
        print(f"\n\nLogged in as {user.role.upper()}")
        return user
    else:
        print("Invalid credentails.")
        return None