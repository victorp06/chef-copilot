# app/models.py

from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

# Define the association table for the many-to-many relationship between User and ShoppingList
user_shopping_list_association = Table(
    'user_shopping_list_association',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('shopping_list_id', ForeignKey('shopping_lists.id'), primary_key=True)
)

shopping_list_item = Table(
    'shopping_list_item',
    Base.metadata,
    Column('shopping_list_id', Integer, ForeignKey('shopping_lists.id')),
    Column('item_id', Integer, ForeignKey('items.id'))
)

# Define association table for Recipe-Ingredient relationship
recipe_ingredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('item_id', Integer, ForeignKey('items.id'))
)

# Define association table for MealPlan-Recipe relationship
meal_plan_recipe = Table(
    'meal_plan_recipe',
    Base.metadata,
    Column('meal_plan_id', Integer, ForeignKey('meal_plans.id')),
    Column('recipe_id', Integer, ForeignKey('recipes.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    joined = Column(DateTime, default=datetime.utcnow())
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    shopping_lists = relationship("ShoppingList", secondary="user_shopping_list_association")


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, default=0)
    expiration_date = Column(Date, nullable=True)

class ShoppingList(Base):
    __tablename__ = 'shopping_lists'
    id = Column(Integer, primary_key=True, index=True)
    items = relationship("Item", secondary="shopping_list_item")

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = relationship("Item", secondary=recipe_ingredient)
    steps = Column(String)

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    recipes = relationship("Recipe", secondary="meal_plan_recipe")
