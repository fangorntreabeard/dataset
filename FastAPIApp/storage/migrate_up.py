from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

Base = declarative_base()
SQLALCHEMY_DATABASE_URL = "postgresql://admin:1234@localhost:5432/asap"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# ForeignKey(User.id)


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    phone_number = Column(String)
    is_admin_ = Column(Boolean)


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)


class Purchase(Base):
    __tablename__ = "Purchase"
    id = Column(Integer, primary_key=True, index=True)
    User_id = Column(Integer,  ForeignKey(User.id))
    Product_id = Column(Integer, ForeignKey(Product.id))


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
