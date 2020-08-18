from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey,Float,Text

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text(20), nullable=False)
    password = Column(Text(20), nullable=False)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text(20), nullable=False)


class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True)
    name = Column(Text(20), nullable=False)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Text(5), primary_key=True)
    name = Column(Text(20), nullable=False)
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    price = Column(Float, nullable=False)
    description = Column(Text(100), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

class Cart(Base):
    __tablename__ = 'carts'
    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Text(5), ForeignKey('items.id'), nullable=False)
    user_id = Column(Text(5), ForeignKey('users.id'), nullable=False)
    quantity = Column(Integer, nullable=False)







