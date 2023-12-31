from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'users'
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String(250))
    email= Column(String(250))
    username= Column(String(250))
    password= Column(String(250))
    address= Column(String(250))
    role_id = Column(Integer, ForeignKey('roles.id'))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Role(Base):
    __tablename__ = 'roles'
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String(250))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class Product(Base):
    __tablename__='products'
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String(250))
    image= Column(String(250))
    price= Column(Float)
    category_id= Column(Integer,ForeignKey('categories.id'))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Category(Base):
    __tablename__='categories'
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String(250))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Order(Base):
    __tablename__ ='orders'
    id= Column(Integer, primary_key=True, index=True)
    status= Column(Integer)
    name= Column(String(250))
    address= Column(String(250))
    phone= Column(String(250))
    total= Column(Float)
    user_id= Column(Integer, ForeignKey('users.id'))
    order_product = relationship("OrderProduct", backref=backref("orders", cascade="delete"))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class OrderProduct(Base):
    __tablename__ ='order_products'
    id= Column(Integer, primary_key=True, index=True)
    order_id= Column(Integer, ForeignKey('orders.id'))
    product_id= Column(Integer, ForeignKey('products.id'))
    size= Column(String(250))
    quantity= Column(Integer)
    product = relationship("Product")
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



